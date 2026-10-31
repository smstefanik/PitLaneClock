from pathlib import Path
p=Path('index.html')
s=p.read_text()
a=s.index('    <circle cx="300"'); b=s.index('  </svg>',a)
s=s[:a]+'''    <defs>
      <linearGradient id="red" x1="0" y1="0" x2="0.8" y2="1"><stop stop-color="#ff343c"/><stop offset=".3" stop-color="#d7202c"/><stop offset=".68" stop-color="#b51022"/><stop offset="1" stop-color="#e52635"/></linearGradient>
      <linearGradient id="steel" x2=".8" y2="1"><stop stop-color="#252b2d"/><stop offset=".3" stop-color="#c4c6bc"/><stop offset=".48" stop-color="#555c58"/><stop offset=".7" stop-color="#eff1df"/><stop offset="1" stop-color="#404944"/></linearGradient>
      <radialGradient id="dial"><stop stop-color="#fffff6"/><stop offset=".8" stop-color="#f1f2df"/><stop offset="1" stop-color="#dcdfcc"/></radialGradient>
      <linearGradient id="lume" x2="1" y2="1"><stop stop-color="#f9fff7"/><stop offset="1" stop-color="#d4e2da"/></linearGradient>
      <linearGradient id="facet"><stop stop-color="#ff7274" stop-opacity=".45"/><stop offset=".5" stop-color="#d51b28" stop-opacity="0"/><stop offset="1" stop-color="#70000a" stop-opacity=".5"/></linearGradient>
    </defs>
    <g id="bezel"></g>
    <circle cx="300" cy="300" r="245" fill="url(#steel)"/>
    <circle cx="300" cy="300" r="237" fill="url(#dial)" stroke="#c6cabd" stroke-width="2"/>
    <circle cx="300" cy="300" r="207" fill="#242b25"/>
    <circle cx="300" cy="300" r="190" fill="url(#dial)"/>
    <g id="marks"></g>
    <g id="indices" fill="url(#lume)" stroke="#28312b" stroke-width="2.8"></g>
    <g id="bezel-type" fill="none" stroke="#fffef1" stroke-width="2.8" stroke-linecap="square" stroke-linejoin="round"></g>
    <g aria-label="TAG Heuer" transform="translate(254 176)">
      <path d="M0 0 H92 V49 L46 77 L0 49 Z" fill="#e32924" stroke="#b91917" stroke-width="2"/>
      <path d="M3 3 H89 V47 L46 73 L3 47 Z" fill="none" stroke="#ffffed" stroke-width="2"/>
      <path d="M5 5 H87 V30 H5 Z" fill="#23834c"/>
      <g fill="none" stroke="#ffffef" stroke-width="4.5" stroke-linejoin="miter">
        <path d="M10 11 H31 M20.5 11 V25 M35 25 L44 10 H48 L57 25 M38 20 H54 M80 12 H65 V25 H81 V19 H73"/>
      </g>
      <g fill="none" stroke="#fff7e5" stroke-width="2.5" stroke-linejoin="miter">
        <path d="M9 35 V48 M19 35 V54 M9 41 H19 M35 35 H25 V57 L35 63 M25 44 H33 M42 35 V65 L47 68 L52 65 V35 M68 35 H59 V61 L68 56 M59 44 H67 M75 52 V35 H84 V42 L75 45 M79 44 L85 47"/>
      </g>
    </g>
    <g id="formula" fill="none" stroke="#252d27" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-label="Formula 1"></g>
    <g id="hour" class="hand">
      <path d="M293 321 L293 205 L300 176 L307 205 L307 321 L300 328 Z" fill="#252d28" stroke="#111914" stroke-width="1.5"/>
      <path d="M296 264 V210 H304 V264 Z" fill="url(#lume)"/>
      <path d="M295 199 L300 184 L305 199 Z" fill="url(#lume)"/>
      <circle cx="300" cy="300" r="18" transform="translate(0 -87)" fill="url(#lume)" stroke="#28312c" stroke-width="3"/>
      <path d="M300 195 V213 L284.5 222 M300 213 L315.5 222" fill="none" stroke="#28312c" stroke-width="2.5"/>
    </g>
    <g id="minute" class="hand">
      <path d="M293 327 V109 L300 99 L307 109 V327 L300 332 Z" fill="#252d28" stroke="#111914" stroke-width="1.5"/>
      <path d="M295 110 L300 104 L305 110 V228 H295 Z" fill="url(#lume)"/>
    </g>
    <g id="second" class="hand">
      <path d="M298.6 108 L300 96 L301.4 108 V342 L300 348 L296 341 L296 318 H293 V294 H298.6 Z" fill="#ce2634" stroke="#b81827" stroke-width=".5"/>
    </g>
    <circle cx="300" cy="300" r="8" fill="#bd2430" stroke="#3b2822" stroke-width="1.5"/>
    <circle cx="298" cy="298" r="2" fill="#f4847a"/>
'''+s[b:]
a=s.index('  for (var i = 0;');b=s.index('  var hands =',a)
s=s[:a]+'''  function element(parent, name, attrs) {
    var el = document.createElementNS(ns, name);
    Object.keys(attrs).forEach(function (key) { el.setAttribute(key, attrs[key]); });
    parent.appendChild(el); return el;
  }
  var bezel = document.getElementById('bezel');
  var outline = '';
  // Thirty shallow grip scallops, with a broad flat crown between notches.
  for (var n = 0; n <= 720; n++) {
    var angle = n / 720 * Math.PI * 2 - Math.PI / 2;
    var notch = Math.pow((1 + Math.cos(angle * 30)) / 2, 5);
    var radius = 291 - notch * 5;
    outline += (n ? ' L' : 'M') + (300 + Math.cos(angle) * radius) + ' ' + (300 + Math.sin(angle) * radius);
  }
  element(bezel, 'path', {d:outline + ' Z', fill:'url(#red)', stroke:'#8d0c19', 'stroke-width':2});
  for (var f = 0; f < 30; f++) {
    element(bezel, 'path', {d:'M277 10 Q300 20 323 10 L320 53 H280 Z', fill:'url(#facet)', transform:'rotate(' + f * 12 + ' 300 300)'});
  }
  var indices = document.getElementById('indices');
  for (var i = 0; i < 60; i++) {
    var rotation = 'rotate(' + i * 6 + ' 300 300)';
    element(marks, i % 5 === 0 ? 'rect' : 'circle', i % 5 === 0 ?
      {x:297,y:96,width:6,height:13,fill:'url(#lume)',transform:rotation} :
      {cx:300,cy:101,r:4.5,fill:'url(#lume)',transform:rotation});
    if (i % 5 !== 0) element(bezel,'circle',{cx:300,cy:46,r:3.2,fill:'#fffbea',transform:rotation});
  }
  for (var h = 0; h < 12; h++) {
    var rot = 'rotate(' + h * 30 + ' 300 300)';
    if (h % 3 === 0) {
      element(indices,'path',{d:'M277 106 H323 V143 L300 162 L277 143 Z',transform:rot});
      element(indices,'path',{d:'M279 121 H321',fill:'none',transform:rot});
    } else {
      var rad = h * Math.PI / 6;
      element(indices,'circle',{cx:300 + Math.sin(rad)*169,cy:300-Math.cos(rad)*169,r:16});
    }
  }
  // Custom outline lettering keeps the face independent of system fonts.
  var glyphs = {
    '0':'M2 0 H16 Q18 0 18 2 V26 Q18 28 16 28 H2 Q0 28 0 26 V2 Q0 0 2 0 Z',
    '1':'M5 0 H10 V28', '2':'M0 0 H18 V13 H0 V28 H18',
    '3':'M0 0 H18 V28 H0 M2 14 H18', '4':'M0 0 V14 H18 M18 0 V28',
    '5':'M18 0 H0 V14 H18 V28 H0',
    'F':'M0 28 V0 H18 M0 13 H15',
    'O':'M3 0 H15 Q18 0 18 3 V25 Q18 28 15 28 H3 Q0 28 0 25 V3 Q0 0 3 0 Z',
    'R':'M0 28 V0 H15 Q18 0 18 3 V10 Q18 13 15 13 H0 M10 13 L18 28',
    'M':'M0 28 V0 L9 17 L18 0 V28', 'U':'M0 0 V25 Q0 28 3 28 H15 Q18 28 18 25 V0',
    'L':'M0 0 V28 H18', 'A':'M0 28 L8 0 H10 L18 28 M4 18 H14'
  };
  function lettering(parent, text, x, y, scale, spacing) {
    var group = element(parent,'g',{transform:'translate('+x+' '+y+') scale('+scale+')'});
    text.split('').forEach(function(c,j) { if(glyphs[c]) element(group,'path',{d:glyphs[c],transform:'translate('+j*spacing+' 0)'}); });
    return group;
  }
  var bezelType = document.getElementById('bezel-type');
  for(var digit=1; digit<12; digit++) {
    var group = element(bezelType,'g',{transform:'rotate('+digit*30+' 300 300)'});
    lettering(group,String(digit*5).padStart(2,'0'),279,18,1,24);
    element(group,'rect',{x:292,y:50,width:16,height:6,fill:'#fffef1',stroke:'none',rx:0.7});
  }
  element(bezelType,'path',{d:'M282 13 H318 L300 36 Z',fill:'#fffef1',stroke:'none'});
  element(bezelType,'circle',{cx:300,cy:22,r:7,fill:'#c81b2a',stroke:'none'});
  element(bezelType,'rect',{x:292,y:50,width:16,height:6,fill:'#fffef1',stroke:'none',rx:0.7});
  lettering(document.getElementById('formula'),'FORMULA 1',207,378,0.78,28);
'''+s[b:]
p.write_text(s)
