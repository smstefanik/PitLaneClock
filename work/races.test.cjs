const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const calendar = vm.createContext({});
vm.runInContext(fs.readFileSync(path.join(__dirname, '..', 'races.js'), 'utf8'), calendar);
const { races, automaticRaceAt, raceScheduleEnd } = calendar;

assert.equal(races.length, 4);
assert.equal(new Set(races.map(race => race.id)).size, races.length);
for (let i = 0; i < races.length; i++) {
  const race = races[i];
  assert.equal(race.defaultTheme, race.id === 'brazil' ? 'brazil' : race.id === 'las-vegas' ? 'vegas' : race.id === 'qatar' ? 'desert-pearl' : 'yas-marina');
  assert.equal(race.sessions.length, 5);
  for (let j = 0; j < race.sessions.length; j++) {
    const session = race.sessions[j];
    assert.match(session.start, /Z$/);
    assert.match(session.end, /Z$/);
    assert.ok(Date.parse(session.end) > Date.parse(session.start));
    if (j) assert.ok(Date.parse(session.start) >= Date.parse(race.sessions[j - 1].end));
  }
  const end = raceScheduleEnd(race);
  assert.equal(automaticRaceAt(end - 1).id, race.id, 'Keep weekend until its scheduled end');
  assert.equal(automaticRaceAt(end)?.id, races[i + 1]?.id, 'Advance at the final session end');
  assert.equal(automaticRaceAt(Date.parse(race.sessions[0].end)).id, race.id, 'Stay through breaks');
  assert.ok(fs.existsSync(path.join(__dirname, '..', race.flag)));
}
assert.equal(automaticRaceAt(Date.parse('2026-11-08T18:00:00Z')).id, 'brazil');
assert.equal(automaticRaceAt(Date.parse('2026-11-08T22:00:00Z')).id, 'las-vegas');
assert.equal(automaticRaceAt(Date.parse('2027-01-01T00:00:00Z')), null);
// Verify track-local date rollover and published first-session times.
const expected = ['06 Nov 12:30', '19 Nov 16:30', '27 Nov 16:30', '04 Dec 13:30'];
races.forEach((race, i) => {
  const parts = Object.fromEntries(new Intl.DateTimeFormat('en-GB', {
    timeZone: race.timeZone, day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit', hourCycle: 'h23'
  }).formatToParts(new Date(race.sessions[0].start)).map(part => [part.type, part.value]));
  assert.equal(`${parts.day} ${parts.month} ${parts.hour}:${parts.minute}`, expected[i]);
});
console.log('Calendar checks passed: session validity, rollover boundaries, breaks, season end, flags, and track time zones.');
