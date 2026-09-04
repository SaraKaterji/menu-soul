# Soul Beirut Menu Website

This is the **online menu** for Soul Beirut.

Customers scan a QR code (or open a link) and see the food, drinks, and prices on their phone. Staff can update that menu later without reprinting a paper booklet every time a price changes.

We are building this from scratch. The breakfast list is on the page. More categories come next.

---

## Who is this for?

| Who | Why they care |
| --- | --- |
| **Guests** | They sit down, scan the code, and browse breakfast, mains, pizza, drinks, and so on. |
| **Soul Beirut staff** | They need a menu that is easy to open, easy to read, and easy to change when prices move. |
| **Us (building it)** | We are making the site. This file is the “what is this thing” note so nobody gets lost. |

Soul Beirut is a restaurant / cafe. They serve breakfast, saj, salads, mains, sandwiches, pizza, pasta, desserts, and hot and cold drinks.

This website is **not** an ordering app. People do not pay or place orders here. It is just the menu on a screen.

---

## What does it do?

In plain words:

1. Someone opens the website on a phone or computer.
2. They see the Soul Beirut menu.
3. They tap a category (like Pizza, or Hot Drinks).
4. They read the dish name, a short description, and the price.

That is the whole job. No login. No cart. No checkout.

---

## The stack (the tools we use)

| Tool | What it is | What we use it for |
| --- | --- | --- |
| **HTML** | The bones of the page. Headings, sections, lists. | The actual menu page (`index.html`). |
| **Tailwind CSS v4** | A styling kit. You add little class names on tags and they become layout, colors, spacing, fonts. | Making the page look good on phones and desktops. |
| **Tailwind CLI** | A small helper that runs on your computer. | It reads those class names and builds a real CSS file (`src/output.css`). |

That is the full stack for now. HTML + Tailwind. No React. No database. No Prettier.

We use the official vanilla install: `tailwindcss` + `@tailwindcss/cli`. Right now that is **Tailwind v4.3.3**.

---

## Fonts (the typefaces)

These live in the `fonts` folder. You do not load them from Google. You just put a class on the tag.

| Class | Font | Use it for |
| --- | --- | --- |
| `font-sans` | Gotham Extra Narrow | Normal text, dish names, prices, descriptions. This is the default on the page. |
| `font-display` | Baroneys Textured | Big category titles like BREAKFAST. |
| `font-script` | Bellarina | Fancy script, if we need it. |
| `font-moric` | Moric | Extra display look, if we need it. |
| `font-arabic` | Baloo Bhaijaan 2 | Arabic text. |

---

## Files in this folder

| File | What it is |
| --- | --- |
| `index.html` | The website. Open this file to see the page. |
| `src/input.css` | The tiny starter file. It just says “please include Tailwind.” You almost never touch this. |
| `src/output.css` | The CSS the computer builds. The website reads this. Do not edit this by hand. |
| `package.json` | The shopping list of tools, plus the commands below. |
| `assets/favicon.png` | The little picture in the browser tab. Drop your icon here and name it exactly `favicon.png`. |
| `fonts/` | The restaurant fonts. Tailwind already knows them. |
| `README.md` | This document. You are reading it. |

Ignore the `node_modules` folder if you see it. That is just Tailwind’s toolbox. Do not edit it.

---

## How to work on it (two commands)

You need Node.js on the computer (it is already here). Open a terminal in this folder.

**First time only** (or if you deleted `node_modules`):

```
npm install
```

That downloads Tailwind.

**While you are designing** (keep this running):

```
npm run dev
```

This watches your HTML. When you add or change a Tailwind class, it updates `src/output.css` by itself. Leave that window open. Stop it with Ctrl + C when you are done.

**Before you put the site live:**

```
npm run build
```

That makes a smaller, ready-to-upload CSS file.

---

## How to open and look at it

1. Run `npm run dev` once so the CSS exists (if you have not already).
2. Find `index.html` in this folder.
3. Double-click it.
4. It opens in Chrome, Edge, or Firefox.

You will see the Breakfast section. That is the first real piece of the menu.

If you add new Tailwind classes and the page looks unchanged, refresh the browser. If it still looks wrong, check that `npm run dev` is still running.

If you prefer Cursor: right-click `index.html` → **Reveal in File Explorer** → double-click the file.

---

## Site icon (the tab picture)

1. Take the restaurant icon (a PNG is best).
2. Name it **exactly** `favicon.png`.
3. Put it in the `assets` folder.

The website is already looking for that file. Until you add it, a simple teal square shows instead.

---

## How the page is put together

The page already has the usual website boxes:

| Part | What it will become |
| --- | --- |
| **Header / nav** | Restaurant name at the top, plus buttons to jump to menu sections. |
| **Main** | The actual menu. Categories, dishes, prices. |
| **Footer** | Small extra info at the bottom (hours, address, whatever we decide). |

When we start designing, we fill those boxes. We do not need a new page for each category. One page is enough.

---

## How people will use the finished menu

Typical visit:

1. Sit at the table.
2. Scan the QR code (same link every time).
3. Land on this website.
4. Tap a category.
5. Read the dish and the price.
6. Tell the waiter what they want.

On a computer it is the same page, just wider.

---

## What we are not doing (yet)

| Not this | Why |
| --- | --- |
| Online ordering | This is a menu, not a shop. |
| A login for staff | Keep it simple. Edits happen in the files, then we put the site live again. |

---

## Going live later

When the site looks right, we upload this folder to the **existing** Soul Beirut Netlify site so the old QR code still works.

Do not make a brand new Netlify site. A new site means a new link, and then the printed QR codes would be wrong.

We will write those upload steps when we are ready to publish. No need to worry about that while we build.
