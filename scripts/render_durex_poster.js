/**
 * render_durex_poster.js - Autonomous Durex-Style Poster Canvas Renderer (GitHub Actions Cloud $0)
 * Renders high-impact minimalist marketing posters with dual-layer typography.
 */

const { createCanvas, GlobalFonts } = require('@napi-rs/canvas')
const fs = require('fs')

// Typography defaults
const SANS = '"Noto Sans", "Source Han Sans SC", "Arial", sans-serif'
const PALETTES = {
  brand_red: { bg: '#F8F8F8', ink: '#1F1F1F', hl: '#C8102E', dim: 'rgba(31,31,31,0.52)' },
  midnight_blue: { bg: '#0E1A2E', ink: '#FFFFFF', hl: '#38BDF8', dim: 'rgba(255,255,255,0.60)' },
  studio_black: { bg: '#121212', ink: '#F3F4F6', hl: '#E11D48', dim: 'rgba(243,244,246,0.55)' },
  papyrus_white: { bg: '#F1EBE0', ink: '#2B2724', hl: '#C8102E', dim: 'rgba(43,39,36,0.55)' }
}

const SPECS = {
  '3x4':  { w: 1200, h: 1600, ax: 0.105, ay: 0.120, bodyR: 0.0385, hlMul: 1.72, lh: 1.95 },
  '1x1':  { w: 1200, h: 1200, ax: 0.095, ay: 0.130, bodyR: 0.0455, hlMul: 1.68, lh: 1.85 },
  '9x16': { w: 1080, h: 1920, ax: 0.105, ay: 0.130, bodyR: 0.0520, hlMul: 1.65, lh: 1.85 },
  '16x9': { w: 1920, h: 1080, ax: 0.062, ay: 0.235, bodyR: 0.0345, hlMul: 1.72, lh: 2.00 }
}

async function renderPoster(options) {
  const {
    eyebrow = 'HERMES · STRATEGIC MARKETING',
    headline = '会提问的人，不需要更好的模型。',
    highlight = '会提问',
    subtext = '试一百把钥匙，不如问对一次。',
    theme = 'brand_red',
    ratio = '3x4',
    output = 'poster.png',
    brandTag = 'HERMES AGENT'
  } = options

  const palette = PALETTES[theme] || PALETTES.brand_red
  const spec = SPECS[ratio] || SPECS['3x4']
  const { w, h, ax, ay, bodyR, hlMul, lh } = spec

  const cv = createCanvas(w, h)
  const ctx = cv.getContext('2d')

  // Background
  ctx.fillStyle = palette.bg
  ctx.fillRect(0, 0, w, h)

  const body = Math.round(w * bodyR)
  const hl = Math.round(body * hlMul)
  const x = w * ax
  let y = h * ay

  // 1. Eyebrow
  ctx.textAlign = 'left'
  ctx.textBaseline = 'alphabetic'
  ctx.fillStyle = palette.dim
  ctx.font = `600 ${Math.round(body * 0.60)}px ${SANS}`
  ctx.fillText(eyebrow, x, y)
  y += body * 2.0

  // 2. Headline with highlight split
  ctx.textAlign = 'left'
  if (headline.includes(highlight) && highlight) {
    const parts = headline.split(highlight)
    let cx = x

    // Pre-highlight
    if (parts[0]) {
      ctx.font = `${body}px ${SANS}`
      ctx.fillStyle = palette.ink
      ctx.fillText(parts[0], cx, y)
      cx += ctx.measureText(parts[0]).width
    }

    // Highlight word
    ctx.font = `bold ${hl}px ${SANS}`
    ctx.fillStyle = palette.hl
    ctx.fillText(highlight, cx, y)
    cx += ctx.measureText(highlight).width

    // Post-highlight
    if (parts[1]) {
      ctx.font = `${body}px ${SANS}`
      ctx.fillStyle = palette.ink
      ctx.fillText(parts[1], cx, y)
    }
  } else {
    ctx.font = `bold ${hl}px ${SANS}`
    ctx.fillStyle = palette.ink
    ctx.fillText(headline, x, y)
  }

  // 3. Subtext
  y += body * 1.8
  ctx.font = `${Math.round(body * 0.65)}px ${SANS}`
  ctx.fillStyle = palette.dim
  ctx.fillText(subtext, x, y)

  // 4. Centered Logo Badge at bottom
  const logoY = h - h * 0.08
  const cx = w / 2
  ctx.textAlign = 'center'
  ctx.fillStyle = palette.dim
  ctx.font = `bold ${Math.round(body * 0.55)}px ${SANS}`
  ctx.fillText(brandTag, cx, logoY)

  const buf = cv.toBuffer('image/png')
  fs.writeFileSync(output, buf)
  console.log(`✅ Durex-style Poster rendered: ${output} (${w}x${h} ratio: ${ratio})`)
}

// CLI argument execution
const args = process.argv.slice(2)
const params = {
  eyebrow: args[0] || 'HERMES · STRATEGIC MARKETING',
  headline: args[1] || 'Người hiểu luật chơi, không cần phải chạy đua.',
  highlight: args[2] || 'hiểu luật chơi',
  subtext: args[3] || 'Đánh trúng một điểm, gãy cả một thành trì.',
  theme: args[4] || 'brand_red',
  ratio: args[5] || '3x4',
  output: args[6] || 'durex_poster.png'
}

renderPoster(params)
