<template>
  <div class="space-bg">
    <div class="stars layer-1"></div>
    <div class="stars layer-2"></div>
    <div class="stars layer-3"></div>

    <div class="planet-img sun"></div>
    <div class="planet-group">
      <div class="planet-img jupiter"></div>
      <div class="planet-img saturn"></div>
      <div class="planet-img earth"></div>
      <div class="planet-img moon"></div>
      <div class="planet-img mars"></div>
      <div class="planet-img mercury"></div>
      <div class="planet-img venus"></div>
      <div class="planet-img uranus"></div>
      <div class="planet-img neptune"></div>
    </div>

    <div class="app">
      <header class="hero">
        <h1 aria-label="Astrology Report Generator">
          <span class="sigil">✶</span>
          Astrology Report Generator
          <span class="sigil">✶</span>
        </h1>
          <p class="tagline">Destiny • Planets • Synastry</p>
          <p class="subtagline">Generated with OpenAI API · GPT-4.1</p>
      </header>

      <section class="form-card">
        <form @submit.prevent="generateBasic">
          <h2>Primary Person</h2>

          <div class="form-grid">
            <label>
              <span>Name</span>
              <input v-model="formData.name" placeholder="e.g. Jane Doe" />
            </label>

            <label>
              <span>Birthday</span>
              <input type="date" v-model="formData.birthday" />
            </label>

            <label>
              <span>Birth Time</span>
              <input type="time" v-model="formData.time" />
            </label>

            <label>
              <span>Birthplace</span>
              <input v-model="formData.birthplace" placeholder="City, Country" />
            </label>

            <label>
              <span>Gender</span>
              <select v-model="formData.gender">
                <option value="Not Provided" selected>Not Provided</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </label>
          </div>

          <div class="divider"><span>Synastry</span></div>

          <h3>Second Person</h3>
          <div class="form-grid">
            <label>
              <span>Name</span>
              <input v-model="formData.second_name" placeholder="e.g. John Smith" />
            </label>

            <label>
              <span>Birthday</span>
              <input type="date" v-model="formData.second_birthday" />
            </label>

            <label>
              <span>Birth Time</span>
              <input type="time" v-model="formData.second_time" />
            </label>

            <label>
              <span>Birthplace</span>
              <input v-model="formData.second_birthplace" placeholder="City, Country" />
            </label>

            <label>
              <span>Gender</span>
              <select v-model="formData.second_gender">
                <option value="Not Provided" selected>Not Provided</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </label>
          </div>

          <div class="actions">
            <button class="btn primary" type="submit" @click="generateBasic">
              ✨ Generate Basic Report (Free)
            </button>
            <button class="btn glow" type="button" @click="generateExtra">
              🔮 Unlock Love &amp; Wealth (Paid)
            </button>
            <button class="btn outline" type="button" @click="generateCompatibility">
              💞 Compatibility Report
            </button>
          </div>
        </form>
      </section>

      <section v-if="basicReport" class="report-card">
        <h2>Basic Report</h2>
        <div v-html="basicReport" class="report markdown-table"></div>
      </section>

      <section v-if="extraReport" class="report-card">
        <h2>Love &amp; Wealth Report</h2>
        <div v-html="extraReport" class="report markdown-table"></div>
      </section>

      <section v-if="compatibilityReport" class="report-card">
        <h2>Compatibility Report</h2>
        <div v-html="compatibilityReport" class="report markdown-table"></div>
      </section>

      <footer class="footer">
        <span>© {{ new Date().getFullYear() }} MINGEEN</span>
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const formData = ref({
  name: "",
  gender: "Not Provided",
  birthday: "",
  time: "",
  birthplace: "",

  second_name: "",
  second_birthday: "",
  second_time: "",
  second_birthplace: "",
  second_gender: "Not Provided"
})

const basicReport = ref('')
const extraReport = ref('')
const compatibilityReport = ref(null)

const cleanMarkdown = (rawText) => {
  if (!rawText) return ''
  return rawText
    .replace(/```(html|markdown)?/g, '')
    .replace(/^#+\s?/gm, '')
    .replace(/^---$/gm, '')
    .trim()
}

const generateBasic = async () => {
  try {
    // const res = await axios.post('http://127.0.0.1:10000/generate-basic-report', formData.value)
    const res = await axios.post(`${API_BASE}/generate-basic-report`, formData.value)
    basicReport.value = cleanMarkdown(res.data.result)
  } catch (err) {
    console.error('Basic Report Error:', err)
    basicReport.value = '<p>Basic report failed to load.</p>'
  }
}

const generateExtra = async () => {
  try {
    // const res = await axios.post('http://127.0.0.1:10000/generate-extra-report', formData.value)
    const res = await axios.post(`${API_BASE}/generate-extra-report`, formData.value)
    extraReport.value = cleanMarkdown(res.data.result)
  } catch (err) {
    console.error('Extra Report Error:', err)
    extraReport.value = '<p>高级报告加载失败</p>'
  }
}

const generateCompatibility = async () => {
  try {
    // const res = await axios.post('http://127.0.0.1:10000/generate-compatibility-report', formData.value)
    const res = await axios.post(`${API_BASE}/generate-compatibility-report`, formData.value)
    compatibilityReport.value = cleanMarkdown(res.data.result)
  } catch (err) {
    console.error('Compatibility Error:', err)
    compatibilityReport.value = '<p>Compatibility report failed to load.</p>'
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=EB+Garamond:wght@400;500;600&display=swap');

:root{
  --font-display: "Cinzel", ui-serif, Georgia, serif;
  --font-body: "EB Garamond", ui-serif, Georgia, serif;
  --group-shift: 2.5vw;   
  --group-time: 18s; 
}

html, body { font-family: var(--font-body); }

.space-bg {
  position: fixed; 
  inset: 0;
  min-height: 100vh;
  overflow-x: hidden;
  background:
    radial-gradient(1200px 600px at 60% -10%, #13255d 0%, rgba(19,37,93,0) 60%),
    radial-gradient(900px 500px at 10% 10%, #0f204a 0%, rgba(15,32,74,0) 65%),
    /* add fallbacks for CSS vars */
    linear-gradient(180deg, var(--bg-mid, #0a1a3a) 0%, var(--bg-deep, #060b1a) 70%);
  color: var(--ink, #e6ecff);
  z-index: 0;          
}

.app{ position: relative; z-index: 1; } /* content above bg */

.hero h1 {
  font-family: var(--font-display);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-weight: 800;
  /* celestial gradient */
  background: linear-gradient(92deg, #f2f5ff 0%, #d9e0ff 35%, #e8d8ff 65%, #f2f5ff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  text-shadow:
    0 0 18px rgba(160, 190, 255, .18),
    0 0 36px rgba(130, 170, 255, .10);
}

.sigil {
  display: inline-block;
  font-size: 0.8em;
  margin: 0 0.35em;
  opacity: .9;
  filter: drop-shadow(0 0 6px rgba(190,210,255,.35));
  animation: sigil-twinkle 3.6s ease-in-out infinite;
}
@keyframes sigil-twinkle {
  0%, 100% { transform: translateY(0) rotate(0deg); opacity: .9; }
  50%      { transform: translateY(-1px) rotate(8deg); opacity: 1; }
}

.tagline {
  font-family: var(--font-display);
  font-size: 13px;
  letter-spacing: .20em;
  text-transform: uppercase;
  color: var(--muted);
  margin-top: 8px;
}

.subtagline {
  margin-top: 6px;
  font-size: 12px;
  letter-spacing: .12em;
  font-variant-caps: all-small-caps;
  color: rgba(200, 210, 255, .85);
  opacity: .95;
  text-shadow: 0 0 10px rgba(140, 180, 255, .16);
}

.stars {
  position: fixed;
  inset: -200px;
  pointer-events: none;
  background-repeat: repeat;
  opacity: .55;
  animation: drift linear infinite;
}

.layer-1 {
  background-image:
    radial-gradient(2px 2px at 20% 30%, rgba(255,255,255,.8) 45%, transparent 46%),
    radial-gradient(1px 1px at 70% 60%, rgba(255,255,255,.6) 45%, transparent 46%),
    radial-gradient(1.5px 1.5px at 40% 80%, rgba(255,255,255,.7) 45%, transparent 46%),
    radial-gradient(1px 1px at 85% 20%, rgba(255,255,255,.5) 45%, transparent 46%);
  background-size: 600px 600px;
  animation-duration: 140s;
}

.layer-2 {
  background-image:
    radial-gradient(1px 1px at 10% 50%, rgba(255,255,255,.6) 45%, transparent 46%),
    radial-gradient(2px 2px at 90% 40%, rgba(255,255,255,.75) 45%, transparent 46%),
    radial-gradient(1.2px 1.2px at 55% 15%, rgba(255,255,255,.65) 45%, transparent 46%);
  background-size: 800px 800px;
  animation-duration: 200s;
  opacity: .35;
}

.layer-3 {
  background-image:
    radial-gradient(1px 1px at 30% 70%, rgba(255,255,255,.45) 45%, transparent 46%),
    radial-gradient(1px 1px at 75% 85%, rgba(255,255,255,.4) 45%, transparent 46%);
  background-size: 1000px 900px;
  animation-duration: 260s;
  opacity: .25;
}

@keyframes drift {
  from { transform: translateY(0) }
  to   { transform: translateY(200px) }
}

.planet {
  position: fixed;
  border-radius: 50%;
  filter: drop-shadow(0 0 20px rgba(140,170,255,.35))
          drop-shadow(0 0 60px rgba(140,170,255,.25));
  pointer-events: none;
  opacity: .85;
}
.planet::after {
  content: "";
  position: absolute;
  inset: -8%;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, rgba(255,255,255,.35), transparent 40%);
}

@keyframes float {
  0%, 100% { transform: translateY(0) translateX(0) }
  50%      { transform: translateY(-96px) translateX(10px) } /* slightly bigger arc */
}
@keyframes float-fast {
  0%, 100% { transform: translateY(0) translateX(0) }
  50%      { transform: translateY(-86px) translateX(16px) } /* faster feel with larger swing */
}

.stars, .planet { position: fixed; pointer-events: none; }

.app {
  width: 100%;
  display: grid;
  grid-template-rows: auto auto 1fr auto;
  place-items: center;
  padding: 48px 16px 64px;
  position: relative; z-index: 1;
}

.hero {
  text-align: center;
  margin-bottom: 24px;
}
.hero h1 {
  font-size: clamp(28px, 4vw, 44px);
  line-height: 1.1;
  letter-spacing: 0.3px;
  margin: 0;
  background: linear-gradient(90deg, #e6ecff 0%, #cfdcff 40%, #dbcfff 65%, #e6ecff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  text-shadow: 0 0 24px rgba(138,182,255,.25);
}
.tagline {
  color: var(--muted);
  margin-top: 8px;
  font-size: 14px;
  letter-spacing: .2em;
  text-transform: uppercase;
}

.space-bg, .space-bg .app {
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

.form-card {
  background: linear-gradient(
    180deg,
    rgba(16, 28, 62, 0.75),
    rgba(14, 24, 54, 0.65)
  );
  border: 1px solid var(--border, rgba(138, 182, 255, 0.25));
  border-radius: var(--radius, 18px);
  box-shadow: var(--shadow, 0 10px 30px rgba(0,0,0,.35), 0 0 60px rgba(130,170,255,.12));
  backdrop-filter: blur(8px) saturate(115%);
  -webkit-backdrop-filter: blur(8px) saturate(115%);
  padding: 20px
}

.form-card h2,
.form-card h3 {
  font-family: var(--font-display, "Cinzel", ui-serif, Georgia, serif);
  text-transform: uppercase;
  letter-spacing: .10em;
  font-weight: 800;
  line-height: 1.2;
  /* soft celestial glow */
  background: linear-gradient(92deg, #f2f5ff 0%, #d9e0ff 35%, #e8d8ff 65%, #f2f5ff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  text-shadow:
    0 0 16px rgba(160,190,255,.16),
    0 0 28px rgba(130,170,255,.10);
}

/* Label captions above fields */
.form-card label span {
  font-family: var(--font-display, "Cinzel", ui-serif, Georgia, serif);
  font-variant-caps: all-small-caps;
  letter-spacing: .20em;
  font-size: 12.5px;
  color: rgba(205, 215, 255, .92);
  text-shadow: 0 0 8px rgba(140,170,255,.12);
}

/* Field text */
.form-card input,
.form-card select,
.form-card textarea {
  font-family: var(--font-body, "EB Garamond", ui-serif, Georgia, serif);
  font-size: 16px;
  letter-spacing: .02em;
  color: #f1f4ff;                 /* readable on dark bg */
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(173,199,255,.50);
}

/* Placeholder style = softer, slightly italic */
.form-card input::placeholder,
.form-card textarea::placeholder {
  color: #d8e0ff;
  opacity: .85;
  font-style: italic;
  letter-spacing: .03em;
}

/* Focus = brighter ink + aura */
.form-card input:focus,
.form-card select:focus,
.form-card textarea:focus {
  border-color: rgba(173,199,255,.85);
  background: rgba(255,255,255,.16);
  box-shadow: 0 0 0 4px rgba(138,182,255,.18);
  color: #ffffff;
}
label {
  display: grid;
  gap: 6px;
  font-size: 13px;
  color: var(--muted);
}

input, select {
  appearance: none;
  background: rgba(255,255,255,.12);
  color: var(--ink);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 12px 12px;
  font-size: 15px;
  outline: none;
  transition: border-color .2s, box-shadow .2s, background .2s;
}
input::placeholder { color: #a9b7e6; opacity: .7; }

input:focus, select:focus {
  border-color: rgba(173,199,255,.7);
  box-shadow: 0 0 0 4px rgba(138,182,255,.12);
  background: rgba(255,255,255,.16);
  cursor: pointer;
}

/* Divider */
.divider {
  position: relative;
  margin: 34px 0 20px;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(138,182,255,.4), transparent);
}
.divider span {
  position: absolute;
  left: 50%;
  transform: translate(-50%, -50%);
  top: 50%;
  background: linear-gradient(180deg, rgba(6,11,26,1), rgba(6,11,26,.6));
  padding: 0 10px;
  color: var(--muted);
  font-size: 12px;
  letter-spacing: .18em;
  text-transform: uppercase;
}

/* Actions */
.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 14px;
}
.btn {
  cursor: pointer;
  border-radius: 14px;
  padding: 12px 16px;
  font-weight: 700;
  letter-spacing: .3px;
  border: 1px solid var(--border);
  background: rgba(255,255,255,.06);
  color: var(--ink);
  transition: transform .08s ease, box-shadow .2s ease, background .2s ease, border-color .2s ease;
  box-shadow: 0 6px 18px rgba(0,0,0,.25);
}
.btn:hover { transform: translateY(-1px) }
.btn:active { transform: translateY(0) scale(.98) }

.btn.primary {
  background: radial-gradient(120% 120% at 50% 0%, rgba(142,188,255,.35), rgba(142,188,255,.08));
  border-color: rgba(142,188,255,.5);
  box-shadow: 0 10px 24px rgba(138,182,255,.25), inset 0 0 24px rgba(138,182,255,.12);
}
.btn.glow {
  background: radial-gradient(120% 120% at 50% 0%, rgba(202,169,255,.35), rgba(202,169,255,.08));
  border-color: rgba(202,169,255,.5);
  box-shadow: 0 10px 24px rgba(202,169,255,.25), inset 0 0 24px rgba(202,169,255,.12);
}
.btn.outline {
  background: radial-gradient(120% 120% at 50% 0%, rgba(38, 218, 176, 0.35), rgba(202,169,255,.08));
  border-color: rgba(202,169,255,.5);
  box-shadow: 0 10px 24px rgba(202,169,255,.25), inset 0 0 24px rgba(202,169,255,.12);
}

/* ====== Reports ====== */
.report-card {
  width: 720px;
  max-width: calc(100% - 32px);
  margin-top: 18px;
  padding: 18px 18px 20px;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  background: linear-gradient(180deg, rgba(16,28,62,.6), rgba(14,24,54,.55));
  box-shadow: var(--shadow);
  backdrop-filter: blur(8px);
}
.report-card h2 {
  margin: 0 0 10px;
  font-size: 18px;
  color: #e8edff;
}

.report table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}
.report th, .report td {
  border: 1px solid rgba(173,199,255,.2);
  padding: 8px 10px;
  font-size: 14px;
}
.report th { background: rgba(173,199,255,.08); color: #f3f6ff; }
.report td { color: #e5ecff; }

.markdown-table table { table-layout: fixed; }
.markdown-table td:first-child {
  width: 32%;
  font-weight: 700;
  color: #dfe6ff;
}

/* ====== Footer ====== */
.footer {
  margin-top: 20px;
  color: var(--muted);
  font-size: 12px;
}

@media (max-width: 760px) {
  .form-grid { grid-template-columns: 1fr; }
  .actions { flex-direction: column; }
}

.planet-img {
  position: fixed;
  pointer-events: none;
  border-radius: 50%;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  filter: drop-shadow(0 0 18px rgba(140,170,255,.22));
  will-change: transform;
  z-index: 0;
}

@keyframes group-sweep {
  from { transform: translateX(-3vw); }
  to   { transform: translateX( 3vw); }
}

.planet-group {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  animation: group-sweep 12s ease-in-out infinite alternate;
  transform: translateZ(0);
}

.planet-group .planet-img {
  position: absolute;
}

@keyframes float {
  0%, 100% { transform: translateY(0) translateX(0); }
  50%      { transform: translateY(-26px) translateX(10px); }
}
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

.planet-img.sun {
  width: 300px; height: 300px;
  right: 20%; top: 12%;
  background-image: url("/planets/sun.png");
  animation: spin 7.5s ease-in-out infinite, spin 60s linear infinite;
  filter: drop-shadow(0 0 24px rgba(255,210,170,.18));
}

.planet-img.sun::before{
  content:"";
  position:absolute; inset:0;
  background-image:url("/planets/sun.webp");
  background-size:cover; background-position:center; background-repeat:no-repeat;
  border-radius:50%;
  animation: spin 180s linear infinite; /* slow spin */
  filter: drop-shadow(0 0 24px rgba(255,210,170,.18));
}

.planet-img.jupiter {
  width: 200px;
  height: 200px;
  right: 8%;
  top: 45%;
  background-image: url("/planets/jupiter.png");
  animation: spin 7.5s ease-in-out infinite, spin 60s linear infinite;
  filter: drop-shadow(0 0 24px rgba(255, 210, 170, 0.18));
}

.planet-img.jupiter::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: url("/planets/jupiter.webp");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border-radius: 50%;
  animation: spin 180s linear infinite;
  filter: drop-shadow(0 0 24px rgba(255, 210, 170, 0.18));
}

.planet-img.earth {
  width: 300px;
  height: 300px;
  left: 15%;
  top: 65%;
  background-image: url("/planets/earth.png");
  animation: float 7.5s ease-in-out infinite, spin 60s linear infinite;
  filter: drop-shadow(0 0 20px rgba(120, 190, 255, 0.28));
}

.planet-img.moon {
  width: 128px;
  height: 128px;
  left: calc(8% + 10px);
  top: calc(58% + 70px);
  background-image: url("/planets/moon.png");
  animation: float 6s ease-in-out infinite;
  filter: drop-shadow(0 0 10px rgba(220, 220, 255, 0.22));
}

.planet-img.saturn{
  position: fixed; right: 20%; top: 65%;
  width: 250px; height: 250px; background: none; pointer-events: none; z-index: 0;
  animation: sweep-340 22s linear infinite alternate;
}
.planet-img.saturn::before{
  content:""; position:absolute; inset:0;
  background: url("/planets/saturn.png") center/contain no-repeat;
  animation: spin 110s linear infinite;
}

.planet-img.mars {
  width: 180px;
  height: 180px;
  left: calc(13% - 10px);
  top: 220px;
  background-image: url("/planets/mars.png");
  animation: float 7s ease-in-out infinite;
  filter: drop-shadow(0 0 20px rgba(255, 140, 120, 0.22));
}

.planet-img.mercury{
  position: absolute; 
  width: 120px; height: 120px;
  right: 2%; top: 24%;
  background-image: url("/planets/mercury.png");
  background-size: cover; background-position: center; background-repeat: no-repeat;
  animation: sweep-20 16s linear infinite alternate; /* or your float/orbit */
  filter: drop-shadow(0 0 14px rgba(180,180,180,.22));
}
.planet-img.mercury::before{
  content:""; position:absolute; inset:0; border-radius:50%;
  background: inherit; background-size: inherit; background-position: inherit; background-repeat: inherit;
  animation: spin 90s linear infinite;
}

.planet-img.venus{
  position: absolute; 
  width: 120px; height: 120px;
  left: -1%; top: 15%;
  background-image: url("/planets/venus.png");
  background-size: cover; background-position: center; background-repeat: no-repeat;
  animation: sweep-340 18s linear infinite alternate;
  filter: drop-shadow(0 0 18px rgba(240,200,120,.22));
}
.planet-img.venus::before{
  content:""; position:absolute; inset:0; border-radius:50%;
  background: inherit; background-size: inherit; background-position: inherit; background-repeat: inherit;
  animation: spin 120s linear infinite;
}

/* Uranus */
.planet-img.uranus{
  position: absolute;
  width: 100px; height: 100px;
  left: 68%; top: 52%;
  background-image: url("/planets/uranus.png");
  background-size: cover; background-position: center; background-repeat: no-repeat;
  animation: float 9s ease-in-out infinite;           /* keep subtle bob */
  filter: drop-shadow(0 0 18px rgba(150, 230, 255, .22));
}
.planet-img.uranus::before{
  content:""; position:absolute; inset:0; border-radius:50%;
  background: inherit; background-size: inherit; background-position: inherit; background-repeat: inherit;
  animation: spin 140s linear infinite;               /* self-spin only */
}

/* Neptune */
.planet-img.neptune{
  position: absolute;
  width: 180px; height: 180px;
  left: 25%; top: 40%;
  background-image: url("/planets/neptune.png");
  background-size: cover; background-position: center; background-repeat: no-repeat;
  animation: float 10s ease-in-out infinite reverse;
  filter: drop-shadow(0 0 18px rgba(110, 180, 255, .24));
}
.planet-group .planet-img.neptune::before{
  content:""; position:absolute; inset:0; border-radius:50%;
  background: inherit; background-size: inherit; background-position: inherit; background-repeat: inherit;
  animation: spin 160s linear infinite;
}

@media (max-width: 900px) {
  .planet-img.mars { left: -24px; top: 220px; }
}

</style>
