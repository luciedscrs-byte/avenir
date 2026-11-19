function el(tag, props, children) {
  const e = document.createElement(tag);
  Object.assign(e, props || {});
  (children || []).forEach(c => e.appendChild(c));
  return e;
}

function dateFr(iso) {
  return new Date(iso + 'T12:00:00').toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' });
}

function dateCourte(iso) {
  return new Date(iso + 'T12:00:00').toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' });
}

function barres(id, lignes) {
  const conteneur = document.getElementById(id);
  const max = Math.max(...lignes.map(l => l.n), 1);
  lignes.forEach(l => {
    const piste = el('div', { className: 'piste' }, [el('span')]);
    piste.firstChild.style.width = (100 * l.n / max) + '%';
    conteneur.appendChild(el('div', { className: 'barre' }, [
      el('span', { className: 'nom', textContent: l.nom }),
      el('span', { className: 'n', textContent: l.n }),
      piste,
    ]));
  });
}

function courbe(valeurs, largeur, hauteur, etiquette, plafond) {
  const ns = 'http://www.w3.org/2000/svg';
  const max = plafond || Math.max(...valeurs, 1);
  const pts = valeurs.map((v, i) =>
    (i * largeur / Math.max(valeurs.length - 1, 1)).toFixed(1) + ',' + ((hauteur - 2) - (hauteur - 4) * v / max).toFixed(1)).join(' ');
  const svg = document.createElementNS(ns, 'svg');
  svg.setAttribute('viewBox', '0 0 ' + largeur + ' ' + hauteur);
  svg.setAttribute('width', largeur);
  svg.setAttribute('height', hauteur);
  svg.setAttribute('role', 'img');
  svg.setAttribute('aria-label', etiquette);
  const ligne = document.createElementNS(ns, 'polyline');
  ligne.setAttribute('points', pts);
  ligne.setAttribute('fill', 'none');
  ligne.setAttribute('stroke', 'currentColor');
  ligne.setAttribute('stroke-width', '1.5');
  svg.appendChild(ligne);
  return svg;
}

const PAGES = [
  ['index.html', 'Accueil'],
  ['methode.html', 'Méthode'],
  ['offres.html', 'Les offres'],
  ['mouvement.html', 'Comment ça bouge'],
  ['entreprises.html', 'Marché caché'],
  ['formation.html', 'Formation'],
  ['actions.html', 'Conclusion'],
];

// Une seule vue : les vrais CDI et CDD (la vue « toutes les offres » n'est plus proposée).
function vue() {
  return 'emploi';
}

function fichierResume() {
  return vue() === 'emploi' ? 'data/resume_emploi.json' : 'data/resume.json';
}

function fr(n) {
  return Number(n).toLocaleString('fr-FR');
}

function boutonSuite(courante) {
  const i = PAGES.findIndex(p => p[0] === courante);
  if (i < 0 || i >= PAGES.length - 1) return;
  const [href, nom] = PAGES[i + 1];
  const bloc = el('div', { className: 'suite' }, [el('a', { className: 'btn', href, textContent: 'Suite : ' + nom })]);
  const pied = document.querySelector('main > footer');
  if (pied) pied.before(bloc); else document.querySelector('main').appendChild(bloc);
}

function navigation(courante, avecVue) {
  const nav = document.getElementById('nav');
  boutonSuite(courante);
  nav.appendChild(el('a', { className: 'marque', href: 'index.html', textContent: 'avenir' }));
  PAGES.forEach(([href, nom]) => {
    const a = el('a', { href, textContent: nom });
    if (href === courante) a.setAttribute('aria-current', 'page');
    nav.appendChild(a);
  });
}
