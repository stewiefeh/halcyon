/* ============================================================
   HALCYON STEREO - main.js  v1.0.0
   No frameworks. Everything degrades gracefully.
   ============================================================ */
(function () {
  "use strict";

  var d = document;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Toast ---------- */
  var toastEl = null;
  var toastTimer = null;
  function toast(msg) {
    if (!toastEl) {
      toastEl = d.createElement("div");
      toastEl.className = "toast";
      toastEl.setAttribute("role", "status");
      toastEl.setAttribute("aria-live", "polite");
      d.body.appendChild(toastEl);
    }
    toastEl.textContent = msg;
    requestAnimationFrame(function () { toastEl.classList.add("show"); });
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove("show"); }, 3200);
  }

  /* ---------- Year stamp ---------- */
  d.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---------- Lamp switch (theme) ---------- */
  var lampBtn = d.querySelector(".lamp");
  var storedTheme = null;
  try { storedTheme = localStorage.getItem("halcyon-theme"); } catch (e) {}
  if (storedTheme === "evening") d.documentElement.setAttribute("data-theme", "evening");
  if (lampBtn) {
    lampBtn.addEventListener("click", function () {
      var root = d.documentElement;
      var next = root.getAttribute("data-theme") === "evening" ? "day" : "evening";
      if (next === "evening") {
        root.setAttribute("data-theme", "evening");
        try { localStorage.setItem("halcyon-theme", "evening"); } catch (e) {}
        toast("Evening mode. The lamp is on, the whiskey is poured.");
      } else {
        root.removeAttribute("data-theme");
        try { localStorage.removeItem("halcyon-theme"); } catch (e) {}
        toast("Dayroom restored.");
      }
    });
  }

  /* ---------- Mobile nav ---------- */
  var navToggle = d.querySelector(".nav-toggle");
  var nav = d.querySelector(".site-nav");
  if (navToggle && nav) {
    navToggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
      navToggle.textContent = open ? "Close" : "Menu";
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        nav.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.textContent = "Menu";
      }
    });
  }

  /* ---------- Reveal on enter (IntersectionObserver, IO fallback) ---------- */
  var revealEls = d.querySelectorAll(".reveal, .sd-rise-fallback");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Vinyl turntable canvas ---------- */
  var vinyl = d.querySelector(".vinyl-stage canvas");
  if (vinyl && !reduceMotion) {
    var ctx = vinyl.getContext("2d");
    var size = 640;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    vinyl.width = size * dpr;
    vinyl.height = size * dpr;
    ctx.scale(dpr, dpr);
    var angle = 0;
    var speed = 0.011;
    var targetSpeed = speed;
    var playing = true;

    var dpr2 = dpr; // keep naming sane
    function drawVinyl() {
      ctx.save();
      ctx.setTransform(dpr2, 0, 0, dpr2, 0, 0);
      ctx.clearRect(0, 0, size, size);
      var c = size / 2;

      // plinth shadow
      ctx.beginPath();
      ctx.arc(c, c + 8, c * 0.94, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(60,35,20,0.25)";
      ctx.fill();

      // vinyl body
      ctx.beginPath();
      ctx.arc(c, c, c * 0.9, 0, Math.PI * 2);
      var g = ctx.createLinearGradient(c - c * 0.9, c - c * 0.9, c + c * 0.9, c + c * 0.9);
      g.addColorStop(0, "#241a12");
      g.addColorStop(0.35, "#3a2a1c");
      g.addColorStop(0.5, "#1d140c");
      g.addColorStop(0.75, "#33241a");
      g.addColorStop(1, "#241a12");
      ctx.fillStyle = g;
      ctx.fill();

      // grooves (rotating highlight)
      ctx.save();
      ctx.translate(c, c);
      ctx.rotate(angle);
      for (var r = 0.86; r > 0.34; r -= 0.035) {
        ctx.beginPath();
        ctx.arc(0, 0, c * r, 0.3, Math.PI - 0.6);
        ctx.strokeStyle = "rgba(255,220,160,0.07)";
        ctx.lineWidth = 1.4;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(0, 0, c * r, Math.PI + 0.5, Math.PI * 2 - 0.2);
        ctx.strokeStyle = "rgba(0,0,0,0.35)";
        ctx.stroke();
      }
      // label
      ctx.beginPath();
      ctx.arc(0, 0, c * 0.32, 0, Math.PI * 2);
      ctx.fillStyle = "#e0862f";
      ctx.fill();
      ctx.beginPath();
      ctx.arc(0, 0, c * 0.32, 0, Math.PI * 2);
      ctx.strokeStyle = "#f4e8cf";
      ctx.lineWidth = 3;
      ctx.stroke();
      // label text arcs
      ctx.fillStyle = "#3a2410";
      ctx.font = "700 " + (size * 0.035) + "px Anybody, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("HALCYON", 0, -c * 0.13);
      ctx.font = "600 " + (size * 0.026) + "px Figtree, sans-serif";
      ctx.fillText("SIDE A - 33 1/3 RPM", 0, c * 0.2);
      // spindle
      ctx.beginPath();
      ctx.arc(0, 0, c * 0.03, 0, Math.PI * 2);
      ctx.fillStyle = "#f4e8cf";
      ctx.fill();
      // light streak
      ctx.beginPath();
      ctx.moveTo(0, -c * 0.9);
      ctx.lineTo(c * 0.16, -c * 0.3);
      ctx.lineTo(-c * 0.16, -c * 0.3);
      ctx.closePath();
      ctx.fillStyle = "rgba(255,240,210,0.12)";
      ctx.fill();
      ctx.restore();

      // tonearm (static over spinning disc)
      ctx.save();
      ctx.translate(c, c);
      ctx.rotate(-0.62);
      ctx.strokeStyle = "#d9cdb6";
      ctx.lineWidth = 7;
      ctx.lineCap = "round";
      ctx.beginPath();
      ctx.moveTo(c * 0.62, -c * 0.62);
      ctx.lineTo(c * 0.34, -c * 0.05);
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(c * 0.62, -c * 0.62, c * 0.09, 0, Math.PI * 2);
      ctx.fillStyle = "#c9b894";
      ctx.fill();
      // headshell
      ctx.save();
      ctx.translate(c * 0.34, -c * 0.05);
      ctx.rotate(0.5);
      ctx.fillStyle = "#e0862f";
      ctx.fillRect(-c * 0.055, -c * 0.04, c * 0.11, c * 0.08);
      ctx.restore();
      ctx.restore();

      ctx.restore();
    }

    function tick() {
      if (!document.hidden) {
        speed += (targetSpeed - speed) * 0.06;
        angle += speed;
        drawVinyl();
      }
      requestAnimationFrame(tick);
    }
    drawVinyl();
    requestAnimationFrame(tick);

    vinyl.parentElement.addEventListener("click", function () {
      playing = !playing;
      targetSpeed = playing ? speed || 0.011 : 0;
      if (playing && targetSpeed === 0) targetSpeed = 0.011;
      toast(playing ? "Needle down. Side A, 33 1/3." : "Tone arm up. Silence, briefly.");
    });
    vinyl.parentElement.setAttribute("role", "button");
    vinyl.parentElement.setAttribute("tabindex", "0");
    vinyl.parentElement.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        vinyl.parentElement.click();
      }
    });
    // V-key easter egg: fast spin
    d.addEventListener("keydown", function (e) {
      if ((e.key === "v" || e.key === "V") && !e.metaKey && !e.ctrlKey && !e.altKey) {
        var tag = (document.activeElement && document.activeElement.tagName) || "";
        if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;
        targetSpeed = 0.14;
        setTimeout(function () { targetSpeed = 0.011; }, 1600);
        toast("45 RPM. For the fast ones.");
      }
    });
  }

  /* ---------- VU meter canvas ---------- */
  var vu = d.querySelector(".vu-panel canvas");
  if (vu && !reduceMotion) {
    var vctx = vu.getContext("2d");
    var W = 560, H = 240;
    var vdpr = Math.min(window.devicePixelRatio || 1, 2);
    vu.width = W * vdpr; vu.height = H * vdpr;
    vu.style.aspectRatio = W + " / " + H;
    var phase = 0;
    function drawVU() {
      vctx.setTransform(vdpr, 0, 0, vdpr, 0, 0);
      vctx.clearRect(0, 0, W, H);
      // two meters, L and R
      for (var m = 0; m < 2; m++) {
        var cx = m === 0 ? W * 0.27 : W * 0.73;
        var cy = H * 0.82;
        var R = H * 0.62;
        // scale arc
        vctx.beginPath();
        vctx.arc(cx, cy, R, Math.PI * 1.05, Math.PI * 1.95);
        vctx.strokeStyle = "#e9ddc4";
        vctx.lineWidth = 3;
        vctx.stroke();
        // ticks
        for (var i = 0; i <= 10; i++) {
          var a = Math.PI * 1.05 + (Math.PI * 0.9) * (i / 10);
          var x1 = cx + Math.cos(a) * (R - 10), y1 = cy + Math.sin(a) * (R - 10);
          var x2 = cx + Math.cos(a) * (R - 22), y2 = cy + Math.sin(a) * (R - 22);
          vctx.beginPath();
          vctx.moveTo(x1, y1); vctx.lineTo(x2, y2);
          vctx.strokeStyle = i > 7 ? "#e05a3a" : "#e9ddc4";
          vctx.lineWidth = i > 7 ? 3.4 : 2.2;
          vctx.stroke();
        }
        // labels
        vctx.fillStyle = "#e9ddc4";
        vctx.font = "700 11px Anybody, sans-serif";
        vctx.textAlign = "center";
        vctx.fillText(m === 0 ? "L" : "R", cx, cy - R - 8);
        // needle
        var wob = Math.sin(phase + m * 2.1) * 0.5 + Math.sin(phase * 2.3 + m) * 0.28;
        var na = Math.PI * 1.05 + (Math.PI * 0.9) * (0.5 + wob * 0.42);
        vctx.beginPath();
        vctx.moveTo(cx, cy);
        vctx.lineTo(cx + Math.cos(na) * (R - 14), cy + Math.sin(na) * (R - 14));
        vctx.strokeStyle = "#f0e4c8";
        vctx.lineWidth = 2.6;
        vctx.stroke();
        vctx.beginPath();
        vctx.arc(cx, cy, 6, 0, Math.PI * 2);
        vctx.fillStyle = "#c9b894";
        vctx.fill();
      }
      // DB arc labels
      vctx.fillStyle = "rgba(233,221,196,0.75)";
      vctx.font = "600 12px Figtree, sans-serif";
      vctx.textAlign = "center";
      vctx.fillText("-20", W * 0.09, H * 0.42);
      vctx.fillText("0", W * 0.5, H * 0.16);
      vctx.fillText("+3", W * 0.91, H * 0.42);
    }
    function vtick() {
      if (!document.hidden) { phase += 0.05; drawVU(); }
      requestAnimationFrame(vtick);
    }
    requestAnimationFrame(vtick);
  }

  /* ---------- Inventory filters ---------- */
  var invGrid = d.querySelector("[data-inventory]");
  if (invGrid) {
    var cards = Array.prototype.slice.call(invGrid.querySelectorAll(".inv-card"));
    var checks = Array.prototype.slice.call(d.querySelectorAll(".filters input[type=checkbox]"));
    var search = d.querySelector("#inv-search");
    var sortSel = d.querySelector("#inv-sort");
    var countEl = d.querySelector("[data-inv-count]");
    var emptyEl = d.querySelector(".inv-empty");

    function applyFilters() {
      var activeTypes = checks.filter(function (c) { return c.checked; })
        .map(function (c) { return c.value; });
      var q = (search && search.value ? search.value : "").toLowerCase().trim();
      var shown = 0;
      cards.forEach(function (card) {
        var type = card.getAttribute("data-type") || "";
        var text = card.textContent.toLowerCase();
        var okType = activeTypes.length === 0 || activeTypes.indexOf(type) !== -1;
        var okText = !q || text.indexOf(q) !== -1;
        var show = okType && okText;
        card.style.display = show ? "" : "none";
        if (show) shown++;
      });
      if (countEl) countEl.textContent = shown + " of " + cards.length + " pieces";
      if (emptyEl) emptyEl.hidden = shown !== 0;
      if (sortSel && sortSel.value !== "featured") {
        var sorted = cards.slice().sort(function (a, b) {
          var pa = parseFloat(a.getAttribute("data-price") || "0");
          var pb = parseFloat(b.getAttribute("data-price") || "0");
          return sortSel.value === "price-asc" ? pa - pb : pb - pa;
        });
        sorted.forEach(function (c) { invGrid.appendChild(c); });
      }
    }
    checks.forEach(function (c) { c.addEventListener("change", applyFilters); });
    if (search) search.addEventListener("input", applyFilters);
    if (sortSel) sortSel.addEventListener("change", applyFilters);
  }

  /* ---------- FAQ accordion ---------- */
  d.querySelectorAll(".faq-q").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var expanded = btn.getAttribute("aria-expanded") === "true";
      var panel = d.getElementById(btn.getAttribute("aria-controls"));
      btn.setAttribute("aria-expanded", expanded ? "false" : "true");
      if (panel) panel.hidden = expanded;
    });
  });

  /* ---------- Tabs ---------- */
  d.querySelectorAll(".tabs").forEach(function (tabs) {
    var btns = Array.prototype.slice.call(tabs.querySelectorAll(".tab-list button"));
    var panels = Array.prototype.slice.call(tabs.querySelectorAll(".tab-panel"));
    btns.forEach(function (btn, i) {
      btn.addEventListener("click", function () {
        btns.forEach(function (b) { b.setAttribute("aria-selected", "false"); });
        panels.forEach(function (p) { p.hidden = true; });
        btn.setAttribute("aria-selected", "true");
        if (panels[i]) panels[i].hidden = false;
      });
      btn.addEventListener("keydown", function (e) {
        var n = null;
        if (e.key === "ArrowRight") n = btns[(i + 1) % btns.length];
        if (e.key === "ArrowLeft") n = btns[(i - 1 + btns.length) % btns.length];
        if (n) { n.focus(); n.click(); }
      });
    });
  });

  /* ---------- Demo forms (no data leaves the page) ---------- */
  d.querySelectorAll("form[data-demo]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      var ok = form.querySelector(".form-success");
      if (ok) {
        ok.classList.add("show");
        ok.setAttribute("role", "status");
      }
      form.querySelectorAll("input, textarea, select, button").forEach(function (f) {
        if (f.type !== "submit") f.value = "";
      });
      var kind = form.getAttribute("data-demo") || "form";
      var msg = "Noted. This is a demo form: nothing was sent anywhere.";
      if (kind === "reserve") msg = "Seat requested. Demo site, so nothing was actually sent.";
      if (kind === "trade") msg = "Trade-in noted. Demo site, nothing was sent.";
      if (kind === "contact") msg = "Message drafted. Demo site, nothing was sent.";
      toast(msg);
    });
  });

  /* ---------- Scroll progress fallback (no scroll-driven support) ---------- */
  if (!CSS.supports("animation-timeline: scroll()")) {
    var rail = d.querySelector(".progress-rail");
    if (rail) {
      var bar = rail.querySelector(".progress-bar");
      var ticking = false;
      window.addEventListener("scroll", function () {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(function () {
          var max = d.documentElement.scrollHeight - window.innerHeight;
          var p = max > 0 ? window.scrollY / max : 0;
          if (bar) bar.style.transform = "scaleX(" + p + ")";
          ticking = false;
        });
      }, { passive: true });
    }
  }
})();
