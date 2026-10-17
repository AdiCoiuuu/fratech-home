# Fratech Home

A full-screen, glass-morphism Home Assistant dashboard inspired by the Fratech Home reference video, with the **Zurli Family** room renders already wired in.

The project is packaged as **one HACS custom integration** that ships and registers both:

- a sidebar panel (`/fratech-home`) that opens the dashboard full-screen;
- the Lovelace card `type: custom:fratech-home`, registered automatically so it is available in any dashboard.

No `ui-lovelace.yaml`, no manual resource entry, no copy/paste of a 2,000-line YAML dashboard.

![Fratech Home desktop](screenshots/01-home-desktop.jpg)

---

## 1. What is included

| Feature | Implementation |
|---|---|
| Full-screen room backgrounds | 9 optimized renders bundled with the integration, overridable per room |
| Clock widget | Top-left live clock, Romanian/English date, time-of-day greeting |
| 10-module command deck | Acasă · Lumini · Jaluzele · Climă · Camere · Vremea · Energie · Media · Rutine · Sistem |
| Sliding glass pop-ups | Animated, draggable, focus-trapped bottom sheets with backdrop blur |
| Room templates | Curte, Garaj, Hol mare, Hol mic, Bucătărie, Dormitor Adi, Dormitor Adina, Dormitor Alexandra |
| Premium weather | Auto-detected `weather.*`, current conditions, 7 detail tiles, 5-day forecast, sun timeline |
| Energy hub | Live power, consumed energy, savings and mapped appliance sensors |
| Media hub | All TVs, channels and remotes in one global panel |
| Smart routines | Cinema, Noapte, Plecare, Dimineață generated from mapped devices |
| Gate doorbell | Picture event, recording mode, night vision, battery, video switch in Curte |
| Find My family map | OpenStreetMap map with distinct people, battery, status and distance |
| K1C 3D printer | Auto-discovered Creality entities, progress, temperatures, controls and tuning |
| Pill controls | Yellow lights, blue covers, cyan climate, green energy/appliances |
| Active-only mode | Unavailable/unknown entities are hidden; exact duplicate IDs are removed |
| Empty-state skeletons | Rooms/pages without mapped entities still exist and show the final layout |
| Real entity mapping | Only the entities supplied in the brief are pre-mapped; weather is optional/auto-detected |
| Home status | Person, zone, sun timeline, WAN, external IP, tracker, notification channel, updates, Assist, shopping list |
| Lovelace + panel | Same LitElement bundle powers both surfaces |
| HACS install | HACS-ready `hacs.json`, installs from `main`, optional release workflow |

### The new command deck

Every module is visible in the bottom hub, not hidden behind a “more” menu:

- **Acasă** — stats, rooms and quick routines.
- **Lumini / Jaluzele / Climă** — generated global pages.
- **Camere** — all eight room renders.
- **Vremea** — current weather, 7 detail tiles, 5-day forecast and the real sun timeline. It auto-detects the first `weather.*` entity; if none exists it shows a premium empty state instead of fake data.
- **Energie** — live power, total energy, savings and the supplied TV energy sensors.
- **Media** — both televisions, channels and the remote in one panel.
- **Rutine** — Cinema, Noapte, Plecare and Dimineață, generated from whatever is mapped.
- **Sistem** — sun, network, updates, Assist and shopping list.

On desktop the deck is one row of ten. On tablets and phones it becomes a symmetric 5×2 command pad, so all ten stay visible.

The new device experiences are contextual instead of adding four more tiny dock icons:

- **Sonerie poartă** opens with **Curte**.
- **Find My family map** is the hero section of **Acasă**.
- **K1C** opens with **Dormitor Adi**, where the printer physically lives.

This keeps the command deck readable while every device still has a dedicated premium surface.

### Screens

| Home popup | Premium weather | Smart routines |
|---|---|---|
| ![Home popup](screenshots/02-home-sheet.jpg) | ![Weather](screenshots/06-weather.jpg) | ![Routines](screenshots/08-routines.jpg) |

| Energy hub | Media hub | Mobile command deck |
|---|---|---|
| ![Energy](screenshots/07-energy.jpg) | ![Media](screenshots/09-media.jpg) | ![Mobile](screenshots/10-mobile.jpg) |

| Room with devices | Empty room skeleton | Empty lights page |
|---|---|---|
| ![Dormitor Adi](screenshots/03-room-adi.jpg) | ![Empty room](screenshots/04-room-empty.jpg) | ![Lights empty](screenshots/12-lights-empty.jpg) |

| System & network | Mobile weather |
|---|---|
| ![System](screenshots/05-system.jpg) | ![Mobile weather](screenshots/11-weather-mobile.jpg) |

| Find My family map | Gate doorbell | K1C 3D printer |
|---|---|---|
| ![Family map](screenshots/02-home-sheet.jpg) | ![Doorbell](screenshots/13-doorbell.jpg) | ![K1C printer](screenshots/14-printer.jpg) |

| Mobile family map | Mobile doorbell | Mobile printer |
|---|---|---|
| ![Mobile family](screenshots/15-mobile-family.jpg) | ![Mobile doorbell](screenshots/16-mobile-doorbell.jpg) | ![Mobile printer](screenshots/17-mobile-printer.jpg) |

---

## 2. Why an integration instead of only a card?

HACS installs a repository in **one** category. A repository cannot be both an “Integration” and a “Lovelace plugin” at the same time. This repository chooses the stronger path:

1. HACS installs the **integration**.
2. The integration serves the bundled JS from `/fratech_home_static/fratech-home.js`.
3. It registers the Lovelace card resource automatically.
4. It registers a full-screen sidebar panel automatically.
5. The panel fetches its configuration from an authenticated endpoint at `/api/fratech_home/config`.

That is why the result feels like a 1-click dashboard instead of a card plus a manual resource.

> The same `dist/fratech-home.js` can still be used manually as a standalone card (see §5). The integration is simply the zero-YAML route.

---

## 3. Entity inventory (strictly the supplied entities)

The default configuration uses **only** these entity IDs. No mock lights, covers, climate devices or sensors are invented.

### Dormitor Adi

| Group | Entity |
|---|---|
| Media | `media_player.camera_de_zi_televizor_adi` |
| Media | `media_player.dormitor_adi_televizor_adi` |
| Remote | `remote.dormitor_adi_televizor_adi` |
| Energy | `sensor.camera_de_zi_televizor_adi_putere` |
| Energy | `sensor.camera_de_zi_televizor_adi_energie` |
| Energy | `sensor.camera_de_zi_televizor_adi_power_energy` |
| Energy | `sensor.camera_de_zi_televizor_adi_energy_saved` |
| Energy | `sensor.camera_de_zi_televizor_adi_energy_difference` |
| TV channel | `sensor.camera_de_zi_televizor_adi_tv_channel` |
| TV channel | `sensor.camera_de_zi_televizor_adi_tv_channel_name` |

### Curte — gate doorbell

| Purpose | Entity |
|---|---|
| Picture event | `event.soneria_inteligenta_doorbell_picture` |
| Recording mode | `select.soneria_inteligenta_mod_inregistrare` |
| Night vision | `select.soneria_inteligenta_vedere_nocturna` |
| Battery | `sensor.soneria_inteligenta_baterie` |
| Video recording | `switch.soneria_inteligenta_inregistrare_video` |

The event image is shown when the event entity exposes `entity_picture` or `picture`. Selects expose their real `options`; the switch uses `switch.toggle`.

### Whole home / system

| Purpose | Entity |
|---|---|
| Person | `person.adihouse` |
| Zone | `zone.home` |
| Sun | `sun.sun` |
| Next dusk | `sensor.sun_next_dusk` |
| Next midnight | `sensor.sun_next_midnight` |
| Next noon | `sensor.sun_next_noon` |
| Next rising | `sensor.sun_next_rising` |
| Next setting | `sensor.sun_next_setting` |
| WAN status | `binary_sensor.upnp_igd_wan_status` |
| External IP | `sensor.upnp_igd_external_ip` |
| Tracker | `device_tracker.tvb` |
| Notifications | `notify.tvb` |
| Conversation | `conversation.home_assistant` |
| Shopping list | `todo.shopping_list` |
| Updates | `update.swipe_card_update` |
| Updates | `update.terminal_ssh_update` |

### Optional weather

No weather entity was included in the supplied inventory, so the dashboard does **not** hardcode one. It auto-detects the first `weather.*` entity present in Home Assistant. To pin a specific station:

```yaml
global:
  weather: weather.<entity_id>
```

If no weather entity exists, the Vremea module still opens and shows a premium empty state plus the real sun timeline.

### Family / Find My

The family map auto-detects `person.*` and `device_tracker.*` entities that have latitude/longitude. Each person gets a distinct color, battery (when exposed), status and distance from home. To pin only specific trackers:

```yaml
global:
  family:
    auto_discover: false
    trackers:
      - person.adrian_stefan
      - device_tracker.fonex30_yahoo_com
    map_zoom: 13
```

Apple iCloud trackers normally appear as `device_tracker.*` and will be picked up automatically. The map uses OpenStreetMap tiles; set `family.map_tiles: false` if you prefer the offline radar-grid fallback.

### K1C 3D printer

The printer entities were supplied as names, not entity IDs, so K1C uses **auto-discovery**:

- finds the device whose name/model contains `K1C`;
- maps its Creality entities by friendly name (`Print Status`, `Bed Temperature`, `Nozzle Target`, etc.);
- renders progress, camera/preview, temperatures, pause/resume/stop/home/reconnect, light, fans and tuning.

It is attached to **Dormitor Adi** because that is the printer’s area. If auto-discovery is ambiguous, map explicitly:

```yaml
rooms:
  - id: dormitor_adi
    printer:
      device_name: K1C
      auto_discover: false
      entities:
        print_status: sensor.k1c_print_status
        print_progress: sensor.k1c_print_progress
        nozzle_temperature: sensor.k1c_nozzle_temperature
        nozzle_target: number.k1c_nozzle_target
        pause_print: button.k1c_pause_print
```

Supported keys follow the entity list: `bed_target`, `bed_temperature`, `case_fan`, `chamber_temperature`, `current_object`, `current_print_preview`, `filament_status`, `flow_factor`, `flow_rate`, `home`, `light`, `max_bed_temperature`, `max_chamber_temperature`, `max_nozzle_temperature`, `model`, `model_fan`, `nozzle_target`, `nozzle_temperature`, `object_count`, `pause_print`, `print_control`, `print_job_time`, `print_progress`, `print_speed`, `print_status`, `print_time_left`, `printer_camera`, `real_time_flow`, `reconnect`, `resume_print`, `side_fan`, `speed_factor`, `stop_print`, `total_layers`, `used_material_length`, `working_layer`.

### Rooms without smart devices

Garaj, Hol mare, Hol mic, Bucătărie, Dormitor Adina and Dormitor Alexandra intentionally render **complete empty-state popups** with a ghost grid. Their data model is already present:

```yaml
rooms:
  - id: dormitor_adina
    entities:
      lights: []
      covers: []
      climate: []
      media: []
      remote: []
      appliances: []
      sensors: []
```

When devices are added later, only the relevant array changes. The popup, room card, background and responsive layout already exist.

---

## 4. Installation

### A. HACS (recommended)

No release/tag is required. This repository uses `hacs.json` without `zip_release`, so HACS installs directly from the default branch.

1. Create a **public** GitHub repository named `fratech-home`.
2. Upload the project so this path exists exactly:
   ```
   custom_components/fratech_home/manifest.json
   ```
   Do **not** upload a ZIP through the GitHub web UI and do not create an extra `fratech-home` nesting level. The repo root must contain `custom_components`, `hacs.json`, `README.md`.
   Optionally update `documentation`, `issue_tracker` and `codeowners` in `manifest.json` if your GitHub username is not `AdiBUBBLE`.
3. In Home Assistant: **HACS → Integrations → ⋮ → Custom repositories**.
4. Add:
   ```
   https://github.com/<YOUR-GITHUB-USER>/fratech-home
   ```
   Category: **Integration** → **Add**.
5. Open the new **Fratech Home** repository in HACS and press **Download/Install**.
6. Restart Home Assistant.
7. **Settings → Devices & Services → Add Integration → search “Fratech Home” → Submit.**
8. A **Fratech Home** entry appears in the sidebar; the card is already registered for Lovelace.

> The integration is declared as `"integration_type": "service"` and has `"version": "1.2.0"`, `"domain": "fratech_home"`, `config_flow: true`, plus `async_setup` and `async_setup_entry` in `__init__.py`. These are the fields Home Assistant uses to list it in **Add Integration**.

The exact GitHub/HACS click-through is also documented in [docs/github-hacs.md](docs/github-hacs.md). Background files can be changed later in **Configure**.

If **Fratech Home** still does not appear:

1. Check the folder is `/config/custom_components/fratech_home/manifest.json`, not `.../fratech_home/fratech_home/manifest.json`.
2. Open **Settings → System → Logs** and search for `fratech_home` or `Error loading custom integration`.
3. Restart Home Assistant fully (not only reload Lovelace).
4. Hard-refresh the browser (`Ctrl+F5`).
5. Confirm `manifest.json` starts with `"domain": "fratech_home"` and has a `"version"` key.

### B. Studio Code Server drag-and-drop (no GitHub required)

1. Open Studio Code Server.
2. Copy the entire `custom_components/fratech_home` folder into:
   ```
   /config/custom_components/fratech_home
   ```
   The final layout must be:
   ```
   /config/custom_components/fratech_home/
     __init__.py
     config_flow.py
     const.py
     frontend.py
     manifest.json
     translations/
     frontend/
       fratech-home.js
       backgrounds/
   ```
3. Restart Home Assistant.
4. **Settings → Devices & Services → Add Integration → Fratech Home**.
5. Open **Fratech Home** in the sidebar.

No Lovelace resource needs to be added manually. The integration registers it during setup.

If you use the supplied `fratech_home.zip`, extract its **contents** directly into `/config/custom_components/fratech_home/`. The ZIP is intentionally flat: `manifest.json` is at the ZIP root, not inside a second `fratech_home/` folder.

### C. Card-only install (optional)

Use this if you already manage Lovelace resources yourself and do not want the sidebar panel.

1. Copy `dist/fratech-home.js` to:
   ```
   /config/www/fratech_home/fratech-home.js
   ```
2. Copy the backgrounds to:
   ```
   /config/www/fratech_home/backgrounds/
   ```
3. Add the resource:
   ```yaml
   url: /local/fratech_home/fratech-home.js?v=1.2.0
   type: module
   ```
4. Use the card:
   ```yaml
   type: custom:fratech-home
   title: Zurli Family
   subtitle: AdiHouse · Smart Home
   greeting_name: Adi
   background_base: /local/fratech_home/backgrounds
   ```
   For a full-screen view, put it in a **Panel (1 card)** dashboard.

---

## 5. Configuration

### 5.1 Card configuration

The card accepts partial overrides. Defaults live in [`src/config.js`](src/config.js); the integration adds branding and background paths on top.

```yaml
type: custom:fratech-home
title: Zurli Family
subtitle: AdiHouse · Smart Home
greeting_name: Adi
language: ro
background_base: /local/backgrounds
backgrounds:
  home: casa.jpg
  dormitor_adina: dormitor_adina.jpg
clock:
  show_seconds: false
global:
  weather: weather.<entity_id>   # optional; otherwise first weather.* is used
  energy: []                    # optional extra energy sensors
rooms:
  - id: dormitor_adina
    entities:
      lights:
        - light.<entity_id>
      covers:
        - cover.<entity_id>
```

Important details:

- `rooms` merges **by `id`**. You never repeat the full room list.
- `entities` merges **by group**. If you send only `lights`, the existing media/remote/energy mappings are preserved.
- Send an explicit empty array (`lights: []`) to clear a group.
- `background` can be an absolute path (`/local/...`) or a URL; otherwise it is resolved against `background_base`.
- Room groups are auto-rendered: `lights`, `covers`, `climate`, `media`, `remote`, `appliances`, `sensors`.
- `global.weather` is optional. The module auto-detects the first `weather.*` entity if this is omitted.
- `global.energy` adds extra energy sensors; the `appliances` groups are always included.
- Routines are generated from mapped entities only. A routine with no matching devices stays visible but disabled under “Necesită mapare”.
- **Active-only mode** is on by default (`features.hide_unavailable: true`). Unavailable/unknown entities are hidden; buttons and event entities whose normal state is `unknown` remain usable.
- Exact duplicate entity IDs are removed at config normalization. The two TV media players are distinct entities and are labelled separately; remove one from `rooms[].entities.media` if your instance reports them as an actual duplicate.

### 5.2 Integration options (no YAML)

Open **Settings → Devices & Services → Fratech Home → Configure**. You can change:

- house title, subtitle, sidebar label;
- Romanian/English UI;
- bundled vs `/local` backgrounds;
- one background filename per room;
- sidebar panel and automatic card registration;
- advanced JSON overrides.

The advanced JSON accepts only these top-level keys:

```json
{
  "rooms": [],
  "global": {},
  "labels": {},
  "remote_commands": {},
  "features": {},
  "clock": {},
  "greeting_name": "Adi"
}
```

Room entries are merged by id, exactly like the card configuration.

### 5.3 Background files

The nine bundled renders are already included:

```
custom_components/fratech_home/frontend/backgrounds/
  casa.jpg          # home / default
  garaj.jpg
  curte.jpg
  hol_mare.jpg
  hol_mic.jpg
  bucatarie.jpg
  dormitor_adi.jpg
  dormitor_adina.jpg
  dormitor_alexandra.jpg
```

Two ways to use your own renders:

1. **Keep bundled mode:** overwrite the files in that folder (same filenames), then hard-refresh the browser.
2. **Use `/local/backgrounds`:** upload your files to `/config/www/backgrounds/`, disable bundled backgrounds in the integration options, set the base to `/local/backgrounds`, and keep/adjust the filenames.

The JS also accepts a direct `/local/...` value for a single room background.

---

## 6. Controls and services used

| UI | Service |
|---|---|
| Light power | `light.turn_on` / `light.turn_off` |
| Light brightness | `light.turn_on` with `brightness_pct` |
| Cover open/stop/close | `cover.open_cover`, `cover.stop_cover`, `cover.close_cover` |
| Cover position | `cover.set_cover_position` |
| Climate power | `climate.turn_on` / `climate.turn_off` |
| Climate target | `climate.set_temperature` |
| Climate mode | `climate.set_hvac_mode` |
| TV power | `media_player.toggle` |
| TV play/pause | `media_player.media_play_pause` |
| TV volume | `media_player.volume_set` |
| Remote power | `remote.toggle` |
| Remote buttons | `remote.send_command` |
| Weather forecast | `weather.get_forecasts` (`daily`, response optional) |
| Energy hub | Read-only from mapped `appliances` sensors |
| Routine Cinema | `light.turn_on` 15%, `cover.close_cover`, `climate.set_temperature` 22, `media_player.turn_on` |
| Routine Noapte / Plecare | `light.turn_off`, `cover.close_cover`, `climate.turn_off`, `media_player.turn_off` |
| Routine Dimineață | `light.turn_on` 30%, `cover.set_cover_position` 30, `climate.set_temperature` 22 |
| Doorbell selects | `select.select_option` |
| Doorbell video | `switch.toggle` |
| K1C print actions | `button.press` |
| K1C fans / light | `fan.toggle` / `light.toggle` (or `switch.toggle` if mapped as a switch) |
| K1C tuning | `number.set_value` |
| Family map | Read-only from `person.*` / `device_tracker.*` |
| Update install | `update.install` |
| Notify test | `notify.send_message` targeting `notify.tvb` |
| Assist | `conversation.process` with `agent_id: conversation.home_assistant` |
| Shopping list | `todo.get_items`, `todo.add_item`, `todo.update_item` |

### Remote command mapping

The D-pad uses `remote.send_command` with configurable command names. Defaults are in `src/config.js`:

```js
remote_commands: {
  up: "UP",
  down: "DOWN",
  left: "LEFT",
  right: "RIGHT",
  select: "CENTER",
  back: "BACK",
  home: "HOME",
  volume_up: "VOLUME_UP",
  volume_down: "VOLUME_DOWN"
}
```

If your TV integration uses different names, override them in the card config or advanced JSON. The two media players are deliberately both shown because both were supplied; label them differently via `labels` if needed.

---

## 7. Empty-state design

A room with zero entities is **not** a dead end:

- its room card is clickable and shows “Pregătit pentru mapare”;
- the popup opens with the correct header, icon, accent and background;
- a ghost grid previews the future layout;
- an expandable “Cum mapez?” panel shows a copyable YAML skeleton.

This is also true for the global **Lumini**, **Jaluzele**, **Climă**, **Energie** and **Media** popups. They are fully generated; they simply have no real entity cards yet.

**Vremea** is a special case: with no weather entity it shows a dedicated empty state, a layout skeleton and the real sun timeline. **Rutine** always render the four moments; routines without mapped actions are visibly disabled and marked “Necesită mapare”.

---

## 8. Architecture

```
fratech-home/
├── custom_components/fratech_home/   # HACS integration
│   ├── __init__.py                   # setup, reload, unload
│   ├── config_flow.py                # initial + options flow
│   ├── const.py
│   ├── frontend.py                   # static path, panel, card resource, API
│   ├── manifest.json
│   ├── translations/
│   └── frontend/
│       ├── fratech-home.js           # built LitElement bundle
│       └── backgrounds/
├── src/                              # readable frontend source
│   ├── fratech-home.js               # card + all views
│   ├── fratech-panel.js              # sidebar panel wrapper
│   ├── config.js                     # rooms, entities, merge logic
│   ├── format.js
│   ├── i18n.js
│   ├── icons.js
│   ├── styles.js
│   └── components/clock.js
├── demo/                             # standalone browser demo with mock hass
├── dist/                             # card-only bundle
├── docs/
├── screenshots/
├── build.mjs
├── hacs.json
└── package.json
```

### Data flow

```
HACS integration
  ├─ serves /fratech_home_static/*
  ├─ registers /api/fratech_home/config (auth required)
  ├─ registers Lovelace resource
  └─ registers sidebar panel
        │
        ▼
<fratech-home-panel> ── fetch config ──► <fratech-home>
                                              │
                                              ├─ normalizeConfig()
                                              ├─ mergeRooms() by id
                                              ├─ render dock / sheet / cards
                                              └─ hass.callService()
```

The UI never reads `.storage`, never edits Lovelace storage, and never needs `configuration.yaml`.

---

## 9. Development

```bash
npm install
npm run build     # dist + integration bundle
npm run watch     # rebuild on change
npm run demo      # serve at http://127.0.0.1:8099/demo/
```

The demo uses a mock `hass` object with the exact supplied entity IDs, so the visual can be reviewed without a Home Assistant instance. It is not part of the integration.

Optional manual release (HACS installs from `main` and does not require this):

```bash
git tag v1.2.0
git push origin v1.2.0
```

The GitHub Action builds the bundle and publishes a `fratech_home.zip` asset. The archive is a convenience artifact; `hacs.json` intentionally does not depend on it.

---

## 10. Troubleshooting

| Symptom | Fix |
|---|---|
| Sidebar entry missing | Restart HA after installing, then add the integration. Check **Settings → Devices & Services** for an error. |
| Background 404 | The integration serves bundled images at `/fratech_home_static/backgrounds`; if you switched to `/local/backgrounds`, upload the files to `/config/www/backgrounds/`. |
| Card does not appear in Lovelace | The card resource is registered automatically unless “Register Lovelace card automatically” is off. Hard-refresh the browser after an update. |
| Remote buttons do nothing | Change `remote_commands` to the command names expected by your TV integration. |
| Assist does not answer | Check that `conversation.home_assistant` supports `conversation.process` and that the user has permission. |
| Shopping list fails | The `todo.get_items` service must be available; check that `todo.shopping_list` is not disabled. |
| Notify test fails | `notify.tvb` must support `notify.send_message` (or use an advanced override to target a modern notify entity). |
| Popup is offset on a tablet | Use the sidebar panel (full bleed) rather than a normal Lovelace section; the panel sets `handle_safe_area` automatically on newer HA releases. |
| Stale UI after update | The JS URL is versioned (`?v=1.2.0`); restart HA and hard-refresh. |

### Security notes

- The config endpoint requires an authenticated Home Assistant session.
- No secrets or tokens are sent to the browser; only entity IDs, labels and background paths.
- The integration does not create users, bypass permissions or call services beyond those listed above.
- Review any advanced JSON before saving; it can change labels and entity mappings, but cannot execute arbitrary code.

---

## 11. Phase 2 — automations

Four advanced scene/automation proposals are documented in [docs/automations.md](docs/automations.md). They are intentionally **not installed** yet; choose the ones you want and they can be wired into the component’s logic in the next iteration.

---

## 12. License

MIT. The bundled room renders belong to the project owner; replace them before redistributing publicly if they are private.
