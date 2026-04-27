<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HTML : balisage & chemins web</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background: linear-gradient(135deg, #e0f0f7 0%, #c8e2ef 100%);
      font-family: system-ui, 'Segoe UI', 'Inter', sans-serif;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .card {
      max-width: 900px;
      width: 100%;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(4px);
      border-radius: 2.5rem;
      padding: 2rem 1.8rem;
      box-shadow: 0 25px 40px -12px rgba(0, 0, 0, 0.25);
      transition: all 0.2s ease;
      border: 1px solid rgba(255,255,255,0.6);
    }

    h1 {
      font-size: 1.9rem;
      font-weight: 800;
      background: linear-gradient(120deg, #1f5e7e, #3083a3);
      background-clip: text;
      -webkit-background-clip: text;
      color: transparent;
      letter-spacing: -0.3px;
      margin-bottom: 0.5rem;
    }

    .tagline {
      font-size: 1rem;
      color: #2c6b8c;
      border-left: 4px solid #4f9fbf;
      padding-left: 1rem;
      margin-bottom: 1.8rem;
      font-weight: 500;
    }

    .grid {
      display: flex;
      flex-wrap: wrap;
      gap: 1.2rem;
      margin: 1.5rem 0 2rem;
    }

    .pillar {
      flex: 1;
      min-width: 150px;
      background: #f5fafd;
      border-radius: 1.5rem;
      padding: 1rem;
      text-align: center;
      transition: transform 0.2s;
    }

    .pillar:hover {
      transform: translateY(-4px);
      background: white;
    }

    .icon {
      font-size: 2rem;
      display: block;
      margin-bottom: 0.4rem;
    }

    .pillar h3 {
      font-size: 1.2rem;
      font-weight: 700;
      color: #1a4e6b;
    }

    .pillar p {
      font-size: 0.8rem;
      color: #2f627f;
      margin-top: 0.3rem;
    }

    code {
      background: #e2edf2;
      padding: 0.2rem 0.4rem;
      border-radius: 12px;
      font-family: monospace;
      font-size: 0.75rem;
      color: #1f5e7e;
    }

    .demo {
      background: #1e2f3a;
      border-radius: 1.5rem;
      padding: 1.2rem;
      margin: 1.8rem 0 1rem;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .demo-code {
      background: #0d1c24;
      padding: 0.8rem;
      border-radius: 1rem;
      font-family: monospace;
      font-size: 0.7rem;
      color: #b3e4f5;
      flex: 2;
      min-width: 160px;
      white-space: pre-wrap;
      word-break: break-word;
    }

    .demo-action {
      flex: 1;
      text-align: center;
    }

    .btn {
      background: linear-gradient(95deg, #2c7da0, #4097b8);
      border: none;
      padding: 0.7rem 1.4rem;
      border-radius: 60px;
      font-weight: bold;
      color: white;
      cursor: pointer;
      font-size: 0.85rem;
      transition: 0.15s;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    .btn:hover {
      transform: scale(1.02);
      background: linear-gradient(95deg, #236c8a, #2c7da0);
    }

    .internal-link {
      margin-top: 0.7rem;
      font-size: 0.75rem;
    }

    .internal-link a {
      color: #9acfdf;
      text-decoration: none;
      border-bottom: 1px dotted;
    }

    .internal-link a:hover {
      color: white;
    }

    .anchor-point {
      background: #e6f3f9;
      margin-top: 1.5rem;
      padding: 0.8rem;
      border-radius: 1.2rem;
      text-align: center;
      font-size: 0.85rem;
      border-left: 5px solid #2c7da0;
    }

    footer {
      text-align: center;
      font-size: 0.7rem;
      color: #4a6f86;
      margin-top: 1.5rem;
    }

    @media (max-width: 550px) {
      .card { padding: 1.5rem; }
      h1 { font-size: 1.6rem; }
    }
  </style>
</head>
<body>
<div class="card">
  <h1>📐 HTML : langage de <em>balisage</em></h1>
  <div class="tagline">🏷️ Poser des repères · 🧭 Marquer un chemin · 🌐 Ouvrir une page web</div>

  <div class="grid">
    <div class="pillar">
      <span class="icon">📍</span>
      <h3>Balises = repères</h3>
      <p><code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;article&gt;</code> structurent le contenu.</p>
    </div>
    <div class="pillar">
      <span class="icon">🔗</span>
      <h3>Chemin & ancres</h3>
      <p>Attribut <code>href</code> + <code>id</code> → chemins hypertexte.</p>
    </div>
    <div class="pillar">
      <span class="icon">🌍</span>
      <h3>Ouvrir une page</h3>
      <p><code>&lt;a target="_blank"&gt;</code> → nouvelle fenêtre.</p>
    </div>
  </div>

  <!-- Démo interactive : balisage + ouverture -->
  <div class="demo">
    <div class="demo-code">
      <span style="color:#ffd966;">&lt;a</span> <span style="color:#9cdcfe;">href</span>=<span style="color:#ce9178;">"https://example.com"</span> <span style="color:#9cdcfe;">target</span>=<span style="color:#ce9178;">"_blank"</span><span style="color:#ffd966;">&gt;</span><br>
      &nbsp;&nbsp;✨ Ouvrir une page web<br>
      <span style="color:#ffd966;">&lt;/a&gt;</span><br>
      <span style="color:#6a9955;">&lt;!-- Ancre interne : #monChemin --&gt;</span>
    </div>
    <div class="demo-action">
      <button class="btn" id="openPageBtn">➡️ Ouvrir une page web</button>
      <div class="internal-link">
        <a href="#" id="goToAnchor">📍 Marquer un chemin (aller au repère)</a>
      </div>
    </div>
  </div>

  <!-- Point d'ancrage (repère interne) -->
  <div id="monChemin" class="anchor-point">
    🧭 <strong>Repère atteint !</strong> — Vous avez suivi le chemin balisé par <code>#monChemin</code>. Le langage HTML permet de créer ces jalons.
  </div>

  <footer>
    💡 HTML n'est pas un langage de programmation, mais un <strong>langage de balisage</strong> : il pose des repères et trace des routes entre les pages.
  </footer>
</div>

<script>
  // Ouverture d'une page web externe (démonstration)
  const openBtn = document.getElementById('openPageBtn');
  if (openBtn) {
    openBtn.addEventListener('click', () => {
      // Ouvre une vraie page web (documentation MDN) dans un nouvel onglet
      window.open('https://developer.mozilla.org/fr/docs/Web/HTML', '_blank');
    });
  }

  // Lien interne pour "marquer un chemin" : défilement vers l'ancre
  const anchorLink = document.getElementById('goToAnchor');
  if (anchorLink) {
    anchorLink.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.getElementById('monChemin');
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'center' });
        // Petit flash visuel
        target.style.transition = 'background 0.2s';
        target.style.background = '#fcf4d9';
        setTimeout(() => target.style.background = '', 600);
      }
    });
  }
</script>
</body>
</html>