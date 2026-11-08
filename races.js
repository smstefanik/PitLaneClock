// F1 sessions for the remaining 2026 calendar, plus São Paulo for debug previews.
// Verified against formula1.com on 2026-11-08. All timestamps are UTC.
// Race end times are the published timetable ends, not live finish detection.
var races = [
  {
    id: 'brazil', round: 20, defaultTheme: 'brazil', name: 'Grande Prêmio de São Paulo',
    officialName: 'FORMULA 1 MSC CRUISES GRANDE PRÊMIO DE SÃO PAULO 2026',
    location: 'São Paulo, Brazil', timeZone: 'America/Sao_Paulo',
    flag: 'assets/brazil.svg', flagAlt: 'Brazil flag',
    source: 'https://www.formula1.com/en/racing/2026/brazil',
    timetable: 'https://www.formula1.com/en/latest/article/formula-1-msc-cruises-grande-premio-de-sao-paulo-2026.3nFWRAkowAY3uUyvw6O0eJ',
    sessions: [
      { name: 'Practice 1', start: '2026-11-06T15:30:00Z', end: '2026-11-06T16:30:00Z' },
      { name: 'Practice 2', start: '2026-11-06T19:00:00Z', end: '2026-11-06T20:00:00Z' },
      { name: 'Practice 3', start: '2026-11-07T14:30:00Z', end: '2026-11-07T15:30:00Z' },
      { name: 'Qualifying', start: '2026-11-07T18:00:00Z', end: '2026-11-07T19:00:00Z' },
      { name: 'Race', start: '2026-11-08T17:00:00Z', end: '2026-11-08T19:00:00Z' }
    ]
  },
  {
    id: 'las-vegas', round: 21, defaultTheme: 'vegas', name: 'Las Vegas Grand Prix',
    officialName: 'FORMULA 1 HEINEKEN LAS VEGAS GRAND PRIX 2026',
    location: 'Las Vegas, United States', timeZone: 'America/Los_Angeles',
    flag: 'assets/united-states.svg', flagAlt: 'United States flag',
    source: 'https://www.formula1.com/en/racing/2026/las-vegas',
    timetable: 'https://www.formula1.com/en/latest/article/formula-1-heineken-las-vegas-grand-prix-2026.1qmWzcBwKK5hkTbYbhVC22',
    sessions: [
      { name: 'Practice 1', start: '2026-11-20T00:30:00Z', end: '2026-11-20T01:30:00Z' },
      { name: 'Practice 2', start: '2026-11-20T04:00:00Z', end: '2026-11-20T05:00:00Z' },
      { name: 'Practice 3', start: '2026-11-21T00:30:00Z', end: '2026-11-21T01:30:00Z' },
      { name: 'Qualifying', start: '2026-11-21T04:00:00Z', end: '2026-11-21T05:00:00Z' },
      { name: 'Race', start: '2026-11-22T04:00:00Z', end: '2026-11-22T06:00:00Z' }
    ]
  },
  {
    id: 'qatar', round: 22, defaultTheme: 'classic', name: 'Qatar Grand Prix',
    officialName: 'FORMULA 1 QATAR AIRWAYS QATAR GRAND PRIX 2026',
    location: 'Lusail, Qatar', timeZone: 'Asia/Qatar',
    flag: 'assets/qatar.svg', flagAlt: 'Qatar flag',
    source: 'https://www.formula1.com/en/racing/2026/qatar',
    timetable: 'https://www.formula1.com/en/latest/article/formula-1-qatar-airways-qatar-grand-prix-2026.3XJyoYSnpJEcuZovstTdcG',
    sessions: [
      { name: 'Practice 1', start: '2026-11-27T13:30:00Z', end: '2026-11-27T14:30:00Z' },
      { name: 'Practice 2', start: '2026-11-27T17:00:00Z', end: '2026-11-27T18:00:00Z' },
      { name: 'Practice 3', start: '2026-11-28T14:30:00Z', end: '2026-11-28T15:30:00Z' },
      { name: 'Qualifying', start: '2026-11-28T18:00:00Z', end: '2026-11-28T19:00:00Z' },
      { name: 'Race', start: '2026-11-29T16:00:00Z', end: '2026-11-29T18:00:00Z' }
    ]
  },
  {
    id: 'abu-dhabi', round: 23, defaultTheme: 'classic', name: 'Abu Dhabi Grand Prix',
    officialName: 'FORMULA 1 ETIHAD AIRWAYS ABU DHABI GRAND PRIX 2026',
    location: 'Abu Dhabi, United Arab Emirates', timeZone: 'Asia/Dubai',
    flag: 'assets/united-arab-emirates.svg', flagAlt: 'United Arab Emirates flag',
    source: 'https://www.formula1.com/en/racing/2026/united-arab-emirates',
    timetable: 'https://www.formula1.com/en/latest/article/formula-1-etihad-airways-abu-dhabi-grand-prix-2026.5mmDojxBdiltjPgeIxAKOq',
    sessions: [
      { name: 'Practice 1', start: '2026-12-04T09:30:00Z', end: '2026-12-04T10:30:00Z' },
      { name: 'Practice 2', start: '2026-12-04T13:00:00Z', end: '2026-12-04T14:00:00Z' },
      { name: 'Practice 3', start: '2026-12-05T10:30:00Z', end: '2026-12-05T11:30:00Z' },
      { name: 'Qualifying', start: '2026-12-05T14:00:00Z', end: '2026-12-05T15:00:00Z' },
      { name: 'Race', start: '2026-12-06T13:00:00Z', end: '2026-12-06T15:00:00Z' }
    ]
  }
];

function raceScheduleEnd(race) {
  return Math.max.apply(null, race.sessions.map(function (session) { return Date.parse(session.end); }));
}

// Keep the weekend selected through every break and until its final F1 session ends.
// Return null after the final loaded race; the UI then shows a season-complete state.
function automaticRaceAt(time) {
  return races.find(function (race) { return Number(time) < raceScheduleEnd(race); }) || null;
}
