from pathlib import Path
p=Path('outputs/clock/index.html');s=p.read_text()
a=s.index('  var bezelType =');b=s.index("    element(group,'rect'",a)
new="""  // Filled bezel glyphs share the proportions and six-unit bars of the traced 30.
  var bezelGlyphs = {
    '0':'M3 0 H17 Q20 0 20 3 V27 Q20 30 17 30 H3 Q0 30 0 27 V3 Q0 0 3 0 Z M6.5 6 Q5.5 6 5.5 7 V23 Q5.5 24 6.5 24 H13.5 Q14.5 24 14.5 23 V7 Q14.5 6 13.5 6 Z',
    '1':'M7 0 H12 Q13 0 13 1 V29 Q13 30 12 30 H8.5 Q7.5 30 7.5 29 V6 H5 Q4 6 4 5 V2 Q4 1 5 1 Z',
    '2':'M2 0 H18 Q20 0 20 2 V16 Q20 18 18 18 H7 Q5.5 18 5.5 19.5 V24 H18.8 Q20 24 20 25.2 V28.8 Q20 30 18.8 30 H2 Q0 30 0 28 V14 Q0 12 2 12 H13 Q14.5 12 14.5 10.5 V7.5 Q14.5 6 13 6 H1.2 Q0 6 0 4.8 V2 Q0 0 2 0 Z',
    '3':'M1.2 0 H18 Q20 0 20 2 V11.5 Q20 14 18.5 15 Q20 16 20 18.5 V28 Q20 30 18 30 H1.2 Q0 30 0 28.8 V25 Q0 24 1.2 24 H13 Q14.5 24 14.5 22.5 V19.5 Q14.5 18 13 18 H1.5 Q.3 18 .3 16.8 V13.2 Q.3 12 1.5 12 H13 Q14.5 12 14.5 10.5 V7.5 Q14.5 6 13 6 H1.2 Q0 6 0 4.8 V1.2 Q0 0 1.2 0 Z',
    '4':'M11.4 0 H15.3 Q16.5 0 16.5 1.2 V18 H18.8 Q20 18 20 19.2 V22.8 Q20 24 18.8 24 H16.5 V28.8 Q16.5 30 15.3 30 H11.7 Q10.5 30 10.5 28.8 V24 H1.5 Q0 24 0 22.5 V19.2 Q0 18.6 .5 17.8 L9.7 1.1 Q10.3 0 11.4 0 Z M5.8 18 H10.5 V9.4 Z',
    '5':'M2 0 H18.8 Q20 0 20 1.2 V4.8 Q20 6 18.8 6 H5.5 V10.5 Q5.5 12 7 12 H18 Q20 12 20 14 V28 Q20 30 18 30 H1.2 Q0 30 0 28.8 V25.2 Q0 24 1.2 24 H13 Q14.5 24 14.5 22.5 V19.5 Q14.5 18 13 18 H2 Q0 18 0 16 V2 Q0 0 2 0 Z'
  };
  var bezelType = document.getElementById('bezel-type');
  for(var digit=1; digit<12; digit++) {
    var group = element(bezelType,'g',{transform:'rotate('+digit*30+' 300 300)'});
    var numerals = element(group,'g',{transform:'translate(278.22 17) scale(.99 .94)',fill:'#fffef1',stroke:'none'});
    String(digit*5).padStart(2,'0').split('').forEach(function(character,index) {
      element(numerals,'path',{d:bezelGlyphs[character],transform:'translate('+index*24+' 0)','fill-rule':'evenodd'});
    });
"""
s=s[:a]+new+s[b:];p.write_text(s)
