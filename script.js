// Theme toggle (persists via localStorage)
(function(){
  const root = document.documentElement;
  const saved = localStorage.getItem('theme');
  if(saved) root.setAttribute('data-theme', saved);
  document.addEventListener('DOMContentLoaded', ()=>{
    const btn = document.querySelector('.theme-toggle');
    if(!btn) return;
    const setIcon = ()=>{ btn.textContent = root.getAttribute('data-theme')==='light' ? '●' : '○'; };
    setIcon();
    btn.addEventListener('click', ()=>{
      const now = root.getAttribute('data-theme')==='light' ? 'dark' : 'light';
      if(now==='dark'){ root.removeAttribute('data-theme'); localStorage.setItem('theme','dark'); }
      else { root.setAttribute('data-theme','light'); localStorage.setItem('theme','light'); }
      setIcon();
    });
  });
})();

// Accessible mobile nav
document.addEventListener('DOMContentLoaded', ()=>{
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.getElementById('primaryNav');

  const closeMenu = ()=>{
    if(!nav || !toggle) return;
    nav.classList.remove('mobile-open');
    toggle.setAttribute('aria-expanded','false');
  };
  const openMenu = ()=>{
    if(!nav || !toggle) return;
    nav.classList.add('mobile-open');
    toggle.setAttribute('aria-expanded','true');
    const firstLink = nav.querySelector('a');
    if(firstLink) firstLink.focus();
  };

  if(toggle && nav){
    toggle.addEventListener('click', ()=>{
      const isOpen = nav.classList.contains('mobile-open');
      isOpen ? closeMenu() : openMenu();
    });
    nav.querySelectorAll('a').forEach(a=>{
      a.addEventListener('click', closeMenu);
    });
    document.addEventListener('keydown', (e)=>{
      if(e.key === 'Escape') { closeMenu(); toggle.focus(); }
    });
    document.addEventListener('click', (e)=>{
      if(nav.classList.contains('mobile-open') && !nav.contains(e.target) && !toggle.contains(e.target)){
        closeMenu();
      }
    });
  }

  // Accordion
  document.querySelectorAll('.acc-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      const item = btn.closest('.acc-item');
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.acc-item').forEach(i=>{ i.classList.remove('open'); i.querySelector('.acc-btn').setAttribute('aria-expanded','false'); });
      if(!isOpen){ item.classList.add('open'); btn.setAttribute('aria-expanded','true'); }
    });
  });

  // Filter
  document.querySelectorAll('.filter-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      document.querySelectorAll('.filter-btn').forEach(b=>{ b.classList.remove('active'); b.setAttribute('aria-selected','false'); });
      btn.classList.add('active');
      btn.setAttribute('aria-selected','true');
      const f = btn.dataset.filter;
      document.querySelectorAll('.comp-item').forEach(item=>{
        item.hidden = (f !== 'all' && item.dataset.cat !== f);
      });
    });
  });
});
