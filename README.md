# MeshCore Window Mount: Heltec LoRa radio for the 2022 Tesla Model 3

A 3D-printed, two-piece window mount that holds a **Heltec WiFi LoRa 32 V3** running **MeshCore** (915 MHz)
inside the car, with the whip antenna outside, for wardriving and mesh coverage mapping. No tools, no drilling,
no adhesive. It hangs on the top edge of the door glass and comes off in seconds.

Designed and tested on a **2022 Tesla Model 3** (front door, frameless glass). The Fusion 360 model is fully
parametric, so you can refit it to another car, radio or coax by changing a few measured numbers (see
[Adapting it to another vehicle](#adapting-it-to-another-vehicle)).

**Version 1.0** (2026-10-17). Printed, fitted and road-tested. The SMA and antenna stack has been driven outside the
window at up to 90 mph.

## How it works

- **Clip:** hooks over the top of the window glass. It carries the SMA bulkhead and whip on a 15° flange outside
  the car, and routes the coax over the glass in a recessed channel so the window seal presses on plastic, not
  the cable.
- **Pocket:** holds the radio in its case on the cabin side, screen facing you, with the USB-C port open at the
  bottom for power. It slides onto the clip on dovetail rails and hangs low enough that the radio and its cable
  clear the roof seal with the window up.

## What to buy

These are the exact parts used for this build:

| Part | Qty | Link |
|---|---|---|
| **Radio:** Heltec WiFi LoRa 32 V3 (ESP32-S3 + SX1262, 915 MHz) kit, with protective case and 1100 mAh battery (2-pack) | 1 kit | [Amazon B0F1CYWVLC](https://www.amazon.com/dp/B0F1CYWVLC) |
| **Coax:** BINGFU SMA female bulkhead to SMA male, RG316, 6 in (15 cm), 2-pack | 1 cable | [Amazon B081BHHPHQ](https://www.amazon.com/dp/B081BHHPHQ) |
| **Antenna:** muzi works 915 MHz LoRa whip, 17 cm | 1 | [Amazon B0D7D6866W](https://www.amazon.com/dp/B0D7D6866W) |
| USB-C cable to a car USB port (power) | 1 | Any. Plug overmold up to about 13 × 7.4 mm fits |
| PLA or PETG filament | ~41 g | Any. **PETG for permanent use:** PLA softens at 55–60 °C, and a parked car in summer gets hotter |

The pocket is sized for the radio **in the kit's case** (32.13 × 28.83 × 63.63 mm). The bulkhead uses a 1/4"-36
thread, a 5/16" nut and two washers (bulkhead cables normally come with the nut and washers). Other radios, cases or coax work if you change the
matching parameters (below).

## Firmware

Flash the radio with the current **MeshCore** firmware from the official sources. The firmware isn't stored here,
so you always get the latest version:

- **Web flasher (easiest):** <https://flasher.meshcore.io>. Use Chrome or Edge (it needs Web Serial). Pick
  *Heltec V3* and the **Companion (BLE)** firmware to pair with the MeshCore phone app.
- **Releases and source:** <https://github.com/meshcore-dev/MeshCore>
- **Project site:** <https://meshcore.io>

## Files

| File | What |
|---|---|
| `stl/clip_front_door_6.65mm.stl` | **Clip for the Model 3 front doors** (6.35 mm laminated glass + 0.3 mm). Already oriented for printing |
| `stl/pocket_heltec_v3.stl` | **Radio pocket.** Already oriented for printing |
| `stl/clip_rear_door_4.10mm.stl` | Clip for the rear doors (3.81 mm glass). Same design, **not print-tested** |
| `stl/glass_thickness_gauge_4.5-8.0mm.stl` | Comb gauge for measuring other cars' glass (slots 4.5–8.0 mm; the notched end is 4.5) |
| `cad/meshcore-window-mount-v1.0.f3d` | **Fusion 360 master model**, fully parametric (both parts plus `REF` bodies for the radio and antenna stack) |
| `cad/clip_v1.0.step`, `cad/pocket_v1.0.step` | STEP solids for other CAD programs (not parametric; front-door clip) |
| `gcode/ender3v2-pla/plate_clip-front+pocket_4h24m.gcode` | Ready-to-print plate for a **stock Creality Ender-3 V2 only** (0.4 mm nozzle, PLA+ at 220/60 °C). 4 h 24 m, 40.7 g |
| `gcode/ender3v2-pla/clip-front_only_2h04m.gcode` | The front clip alone, same printer and settings. 2 h 04 m |
| `tools/orient_for_print.py` | Re-orients a Fusion STL export for printing (Python + trimesh) |

Don't run the G-code on other printers. Slice the STLs yourself.

## Printing

Settings used and tested (OrcaSlicer, 0.4 mm nozzle):

- 0.2 mm layers, **6 walls**, 35 % gyroid infill
- **No supports, no brim.** Every overhang is designed to print without support.
- Elephant-foot compensation about 0.15 mm. The dovetail and radio fits depend on accurate first layers.
- Outer walls slow (about 25 mm/s) for clean fit surfaces
- Bed 60 °C for PLA

**Orientation (the STLs are already set this way):**

- **Clip on its side**, the "WAR DRIVE" end on the bed. Every layer is then a full profile of the clip, so it is
  strongest against the loads it carries and needs no supports.
- **Pocket upright**, floor on the bed.

Print both parts in one plate in about 4.5 h, or the clip alone in about 2 h.

## Assembly and install

1. **Pocket onto the clip:** slide the pocket on from the "MESHCORE" side. The rails enter the slot mouths on its
   "WAR DRIVE" face. It starts easily on the entry chamfers, then becomes a friction fit and stops at the closed
   end.
2. **Antenna:** push the SMA bulkhead up through the flange hole from below. Add the washers and the 5/16" nut
   (the 12 mm spot-face gives the thread enough length), then screw on the whip.
3. **Cable:** run the coax from the bulkhead down through the pass-through hole, over the glass in the recessed
   channel, and down the cabin side to the radio. Leave a small loop.
4. **Radio:** drop the radio in, in its case, SMA end up and screen toward the cabin. Connect the coax and the
   USB-C power cable (through the floor opening).
5. **Hang it:** lower the window about an inch, hang the clip on the glass, and raise the window. Tie the
   pocket's tether tab to the grab handle as a backup.
6. Open and close the door once to check that it stays put. Model 3 windows drop a little when the door opens and
   rise again when it closes.

## Adapting it to another vehicle

Everything is driven by **user parameters**. In Fusion 360, open `cad/meshcore-window-mount-v1.0.f3d` and go to
**Modify → Change Parameters**. Change the values, check that the timeline shows no errors, then export the
`Clip` and `Pocket` bodies as STL (not the `REF` bodies).

### The parameters you'll actually change

| Parameter | v1.0 value | What to measure |
|---|---|---|
| `glass` | 6.65 mm | **Window glass thickness + 0.3 mm.** Measure the top edge of the glass with calipers, or print the comb gauge. Model 3 front 6.35 mm → 6.65; rear 3.81 mm → 4.10 |
| `coax_od` | 2.41 mm | **Outer diameter of your SMA coax.** It sets the cable channel (`cable_w` = coax + 0.39, `cable_d` = coax + 0.59, rounded floor) and the bridge over the glass (coax + 2.09), so the plastic under the cable stays the same thickness. RG316 ≈ 2.5 mm, RG174 ≈ 2.8 mm |
| `radio_w` | 1.265 in (32.13 mm) | Radio width **in its case** (across the screen) |
| `radio_d` | 1.135 in (28.83 mm) | Radio depth in its case (screen to back) |
| `radio_h` | 2.505 in (63.63 mm) | Radio height in its case |
| `radio_drop` | 2.5 in | How far below the top of the glass the radio's top sits. Increase it if the radio or its cable hits the roof seal with the window up. The clip's inner leg grows with it |
| `glass_tilt` | 15° | How far the glass leans in from vertical. It tilts the antenna flange so the whip stands upright |

**Checked in v1.0:** the model rebuilds with no errors and no clip/pocket collision for coax 1.8, 2.5 and 3.0 mm;
glass 4.10 and 5.3 mm; and radios of 30 × 26 × 58 mm and 35 × 30 × 70 mm. Only the front-door Model 3 values have
been printed.

### Fit tuning

| Parameter | v1.0 value | Effect |
|---|---|---|
| `slot_clear` | 0.15 mm/side | Dovetail fit between pocket and clip. Too tight → 0.18, too loose → 0.12 |
| `side_rib_clear` | 0.2 mm/side | Radio fit in the pocket. Lower it (e.g. 0.15) for more grip |
| `usb_from_front` | 0.175 in (4.45 mm) | USB-C port centre from the screen face, for a different radio |
| `clip_w` | 35.52 mm | Clip width along the glass |

Clearances are tuned on one Ender-3 V2. On another printer, print the pair once and adjust `slot_clear` and
`side_rib_clear`.

**Known limitation:** the side-wall text ("WAR DRIVE", "MESHCORE / 915MHz") is placed at fixed sketch positions.
If you change the radio size or `radio_drop`, move those three sketches with the pocket, or delete the text.

## Safety

- Set it up while parked. Don't adjust the radio or phone while driving.
- Mount it on a window that doesn't block your view or mirrors, and don't use one-touch auto-up with the mount
  installed.
- Use the tether. Check the clip for cracks now and then, especially PLA after hot days.
- Make sure your radio settings (frequency and power) are legal where you drive. The US 915 MHz ISM band is
  license-free.

## Version history

| Version | Date | Notes |
|---|---|---|
| **1.0** | 2026-10-17 | First public release. Fit, radio clearance and antenna confirmed in a 2022 Model 3. New `coax_od` parameter |
| 0.1–0.9 | 2026-10-08 → 10-16 | Nine development prints: one-piece to two-piece, dovetail redesign, radio-in-case sizing, curved cable channel, lighter clip, radio lowered to clear the roof seal |

## License

**CC BY-NC-SA 4.0** ([full text](LICENSE)). You may print, share and remix this design for **non-commercial** use,
as long as you credit **Abot Developments** and share your changes under the same license. For commercial use
(selling prints or kits), ask first.

Amazon links are plain product links, not affiliate links. MeshCore, Heltec and Tesla are trademarks of their
owners. This project isn't affiliated with or endorsed by them.
