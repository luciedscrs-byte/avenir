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
  ['metier.html', 'Le métier'],
  ['index.html', 'Les offres'],
  ['mouvement.html', 'Comment il bouge'],
  ['entreprises.html', 'Les entreprises (marché caché)'],
];

function navigation(courante) {
  const nav = document.getElementById('nav');
  PAGES.forEach(([href, nom]) => {
    const a = el('a', { href, textContent: nom });
    if (href === courante) a.setAttribute('aria-current', 'page');
    nav.appendChild(a);
  });
}
