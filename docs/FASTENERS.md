# JammyFox fasteners / 螺丝、螺母、垫片

Updated: 2026-10-12. Applies to CAD Revision A and the confirmed FEETECH ST-3215-C018.

**Use M3 metric socket-head machine screws for the robot structure and horn connections. Use M2.5 only for board mounts that match the actual PCB holes. Keep the original servo centre screws.**

The CAD gives an exact count of horn interfaces and clamp bolt positions. Lengths below are a **nominal fit-trial specification**, not a complete production release. Some frame, foot and enclosure connections still lack matching holes, nut seats or attachment features. The existing SolidWorks/STEP geometry is unchanged by this schedule.

## Standard hardware choices

| Use | Selected specification | Chinese purchase wording |
|---|---|---|
| Main machine screws | M3 x 0.5, ISO 4762 / DIN 912 socket-head cap screw; zinc-plated steel property class 8.8 | 8.8级 镀锌 杯头内六角螺丝 M3 |
| Through-bolt nuts | M3 x 0.5 DIN 985 nylon-insert locknut, nominal 5.5 mm across flats and 4 mm high | M3 镀锌 尼龙防松螺母 |
| Bearing washers | Metal M3 flat washers: 3.2 mm bore, 7 mm OD, 0.5 mm thick | M3 平垫圈 3.2×7×0.5 |
| Horn length adjustment | Metal flat spacer washer: 3.2–3.4 mm bore, 7–8 mm OD, 1.00 mm thick | M3 加厚平垫片 厚1mm |
| Future captive nuts | Ordinary M3 x 0.5 hex nuts, nominal 5.5 mm across flats and 2.4 mm high; quantities await detailing | M3 六角螺母 |
| PCB mounts | Proposed M2.5 x 0.45 screws and brass female-female standoffs; match real boards | M2.5 螺丝 双通铜柱 |

M3 screw length is measured **under the head**, excluding the head. ISO 4762 M3 heads are approximately 5.5 mm diameter and 3 mm high, with a 2.5 mm hex socket. These match the selected head envelope; countersunk screws require a different seat. [Supplier dimensions](https://americas.bossard.com/products/1011936.html). Locknut dimensions: [BelMetric drawing](https://belmetric.com/content/A-PDF_Drawings/NN3SS.pdf).

The Rev A Ø3.4 mm holes are **clearance holes**, not M3 threads. Structural through bolts need metal nuts. Future removable covers can use captured metal nuts after the pockets are added. No heat-set inserts or additional special shafts are required by this proposal. Clamp bolts close the two case halves; they do not automatically attach a clamp to its parent frame.

## Horn connection screws: 120 total

Each of the 30 connected horn faces uses four M3 screws on a 14 mm bolt circle. Neck yaw and tail connect only the front face; the other joints connect both faces.

For every screw in this table, use **one 0.5 mm flat washer plus one 1.0 mm metal spacer washer under the head**. The printed interface spacer remains between the carrier and the metal horn.

Assembly order: screw head → flat washer → 1 mm metal washer → 4 mm printed carrier → printed interface spacer → threaded metal horn.

| ID | Screw length | Printed spacer + carrier (mm) | CAD count | Bulk quantity after fit trial | Location | Purchase links |
|---|---|---|---:|---:|---|---|
| H01 | M3 x 8 | 0.6 + 4 | 4 | 10 | Jaw front horn | [JD search](https://search.jd.com/Search?keyword=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%208%20DIN912&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%208%20DIN912) |
| H02 | M3 x 10 | 2.6 + 4 | 40 | 50 | Both hip-pitch horns; neck-yaw front; tail front | [JD search](https://search.jd.com/Search?keyword=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2010%20DIN912&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2010%20DIN912) |
| H03 | M3 x 12 | 4.6 + 4 | 4 | 10 | Jaw back horn | [JD search](https://search.jd.com/Search?keyword=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2012%20DIN912&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2012%20DIN912) |
| H04 | M3 x 14 | 6.6 + 4 | 40 | 50 | Both hip-roll horns; both neck-pitch horns | [JD search](https://search.jd.com/Search?keyword=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2014%20DIN912&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2014%20DIN912) |
| H05 | M3 x 18 | 10.6 + 4 | 32 | 40 | Both knee horns | [JD search](https://search.jd.com/Search?keyword=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2018%20DIN912&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2018%20DIN912) |

The nominal penetration is `screw length − spacer − carrier − 1.5 mm = 1.9 mm` for all five groups. This is a chosen starting target, **not an approved minimum engagement or permissible protrusion from FEETECH**. The manufacturer shows different horn plate thicknesses: 2.5 mm on the drive horn and 2.1 mm on the passive horn. Rev A simplifies both to 2.5 mm; actual rear spacer stacks therefore need calibration. The original drawing specifies four threaded M3 holes but does not give an allowable screw protrusion into the assembled servo. [Exact C018 drawing, pages 4, 6 and 7](https://www.feetechrc.com/Data/feetechrc/upload/file/20240507/6385067068652648096680943.pdf).

Measure the actual clamped stack and horn-to-case clearance before accepting any length. Target enough sound metal thread engagement while keeping the screw tip clear of the case; use supplier guidance if the horn engagement is insufficient. Do not simply replace a 14 mm screw with 16 mm, or an 18 mm screw with 20 mm: an extra 2 mm of length also needs an extra 2 mm of washer spacing and a fresh head-clearance check.

## Clamps, washers and original servo screws

The following quantities cover the calculated horn/clamp interfaces. PCB rows are proposals. `Bulk quantity` is a pack-size suggestion **after its stated condition is resolved**; zero means reuse the supplied accessory.

| ID | Specification | Nominal count | Bulk quantity | Status | Purchase links |
|---|---|---:|---:|---|---|
| C01 | M3x50; pitch 0.5; ISO 4762 / DIN 912; steel 8.8 zinc plated | 56 | 70 | FIT_SAMPLE_REQUIRED | [JD search](https://search.jd.com/Search?keyword=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2050%20DIN912&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=8.8%20%E9%95%80%E9%94%8C%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2050%20DIN912) |
| C02 | M3x85 nominal; pitch 0.5; same head; availability/stack/clearance to confirm | 8 | 10 | CAD_DETAIL_REQUIRED | [JD search](https://search.jd.com/Search?keyword=%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2085%20%E5%8A%A0%E9%95%BF%20%E8%9E%BA%E4%B8%9D&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20M3%2085%20%E5%8A%A0%E9%95%BF%20%E8%9E%BA%E4%B8%9D) |
| W01 | M3; ISO 7089 / DIN 125 A; ID3.2 x OD7 x thickness0.5mm; metal | 248 | 300 | FIT_SAMPLE_REQUIRED | [JD search](https://search.jd.com/Search?keyword=M3%20%E5%B9%B3%E5%9E%AB%E5%9C%88%203.2%207%200.5%20DIN125&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=M3%20%E5%B9%B3%E5%9E%AB%E5%9C%88%203.2%207%200.5%20DIN125) |
| W02 | Metal ring; ID3.2-3.4 x OD7-8 x thickness1.00mm; verify actual thickness | 120 | 150 | FIT_SAMPLE_REQUIRED | [JD search](https://search.jd.com/Search?keyword=M3%20%E5%8A%A0%E5%8E%9A%20%E5%B9%B3%E5%9E%AB%E7%89%87%20%E5%86%85%E5%BE%843.2%20%E5%A4%96%E5%BE%848%20%E5%8E%9A1mm&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=M3%20%E5%8A%A0%E5%8E%9A%20%E5%B9%B3%E5%9E%AB%E7%89%87%20%E5%86%85%E5%BE%843.2%20%E5%A4%96%E5%BE%848%20%E5%8E%9A1mm) |
| N01 | M3x0.5; DIN 985; nominal AF5.5mm x height4mm; zinc-plated steel | 64 | 80 | FIT_SAMPLE_REQUIRED | [JD search](https://search.jd.com/Search?keyword=M3%200.5%20%E9%98%B2%E6%9D%BE%E8%9E%BA%E6%AF%8D%20DIN985%20%E9%95%80%E9%94%8C&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=M3%200.5%20%E9%98%B2%E6%9D%BE%E8%9E%BA%E6%AF%8D%20DIN985%20%E9%95%80%E9%94%8C) |
| S01 | Original FEETECH M3x6; retain original head and screw supplied with servo | 16 | 0 | REUSE_SERVO_ACCESSORY | [JD search](https://search.jd.com/Search?keyword=%E9%A3%9E%E7%89%B9%20ST3215%20C018%20%E8%88%B5%E7%9B%98%20%E4%B8%AD%E5%BF%83%20%E5%9B%BA%E5%AE%9A%E8%9E%BA%E4%B8%9D%20M3%206&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=%E9%A3%9E%E7%89%B9%20ST3215%20C018%20%E8%88%B5%E7%9B%98%20%E4%B8%AD%E5%BF%83%20%E5%9B%BA%E5%AE%9A%E8%9E%BA%E4%B8%9D%20M3%206) |
| S02 | Original FEETECH PA3.0x5 self-tapping screw; retain supplied screw | 16 | 0 | REUSE_SERVO_ACCESSORY | [JD search](https://search.jd.com/Search?keyword=%E9%A3%9E%E7%89%B9%20ST3215%20C018%20%E5%89%AF%E8%BD%B4%20%E8%88%B5%E7%9B%98%20PA3%205%20%E8%9E%BA%E4%B8%9D&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=%E9%A3%9E%E7%89%B9%20ST3215%20C018%20%E5%89%AF%E8%BD%B4%20%E8%88%B5%E7%9B%98%20PA3%205%20%E8%9E%BA%E4%B8%9D) |
| P01 | M2.5x6; coarse pitch0.45; ISO 4762 / DIN 912; zinc-plated steel | 16 | 20 | BOARD_VARIANT_AND_CAD_DETAIL_REQUIRED | [JD search](https://search.jd.com/Search?keyword=M2.5%206%20%E6%9D%AF%E5%A4%B4%20%E5%86%85%E5%85%AD%E8%A7%92%20%E8%9E%BA%E4%B8%9D&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=M2.5%206%20%E6%9D%AF%E5%A4%B4%20%E5%86%85%E5%85%AD%E8%A7%92%20%E8%9E%BA%E4%B8%9D) |
| P02 | M2.5 female-female brass hex standoff; body8mm; no protruding male stud | 8 | 10 | BOARD_VARIANT_AND_CAD_DETAIL_REQUIRED | [JD search](https://search.jd.com/Search?keyword=M2.5%20%E9%93%9C%E6%9F%B1%20%E5%8F%8C%E9%80%9A%20%E6%AF%8D%E6%AF%8D%208mm&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=M2.5%20%E9%93%9C%E6%9F%B1%20%E5%8F%8C%E9%80%9A%20%E6%AF%8D%E6%AF%8D%208mm) |
| P03 | M2.5 metal flat washer; ID2.7 x OD6 x thickness0.5mm | 16 | 20 | BOARD_VARIANT_AND_CAD_DETAIL_REQUIRED | [JD search](https://search.jd.com/Search?keyword=M2.5%20%E5%B9%B3%E5%9E%AB%E5%9C%88%202.7%206%200.5&enc=utf-8) / [Taobao search](https://s.taobao.com/search?q=M2.5%20%E5%B9%B3%E5%9E%AB%E5%9C%88%202.7%206%200.5) |

For C01, the two printed clamp halves total 42 mm. A 50 mm bolt with two 0.5 mm washers and a 4 mm locknut leaves approximately 3 mm beyond the nut. Check screw-head, nut and tip clearance throughout joint motion; the original motion report did not include hardware.

C02 is a **held proposal**: share a longer bolt through the 42 mm clamp and 34 mm pedestal. The nominal stack is 76 mm, or 78 mm where the 2 mm chassis also lies beneath it. M3 x 85 leaves approximately 4 or 2 mm beyond the locknut. Matching chassis holes, access and anchoring must be finished before ordering this group. M3 x 50 only closes these two clamps if separate accessible nuts and independent pedestal fasteners are designed.

Keep the 16 original M3 x 6 drive-side centre screws and the 16 original PA3.0 x 5 passive-side self-tapping screws. The case drawing labels the passive boss screw PA3.0 x 5; it is not an M3 machine thread. Keep factory case screws installed. Ask the servo supplier for exact replacement accessories if any are missing. The stock M3 x 6 centre screw is not interchangeable with a horn-coupling screw through our carrier/spacer stack.

P01–P03 assume four mounting positions per board. Their 8 mm standoffs would raise the board envelopes relative to Rev A, so board height/connector clearance and holes must be updated. For a nominal 1.6 mm PCB and 3 mm tray, M2.5 x 6 screws with 0.5 mm washers enter the standoff by about 3.9 mm from above and 2.5 mm from below. Verify the actual threaded depths and that opposing screws cannot meet.

## Remaining attachment details

These are outside the 120 horn screws and 64 clamp positions. Their final quantities must be counted after the fastening features are added; no complete-robot purchase total is claimed here.

| Interface | Fastener approach selected | Rev A detail still required |
|---|---|---|
| Split chassis/rails and hip bases | M3 socket-head through bolts, flat washers and metal nuts | Rail attachment holes/bosses, seam connection and hip-base hole alignment; also secure hip-roll cases to their bases |
| Knee, neck-pitch and jaw case attachment | M3 bolts with captured/accessibly mounted nuts | Attach fixed case clamps to their parent carriers/bridge; the existing clamp bolts alone do not create these connections |
| Four rigid feet | M3 through bolts and locknuts | Remove the foot-ear/shin material overlap, provide clamping support and positive anti-rotation; select length after the ear stack is finished |
| Body covers | M3 removable bolts with captured nuts, or long through bolts | Current 73.4 mm posts have plain through bores; captured-nut pockets are absent. A long-bolt approach would use about M3 x 85, but is not released |
| Head lid | M3 removable bolts and metal nuts | Add compression sleeves through the raised lid cavity and accessible/captured nut seats |
| Tail shell/tip, muzzle, ears and cosmetic parts | Short M3 screws and captured nuts where wall/boss thickness permits | Matching bosses/holes and tool access; cosmetic parts are currently separate bodies |
| Battery tray/crossbars and electronics tray | M3 through bolts and metal nuts | Matching anchor holes and battery retention features; tray-to-chassis stack also needs length selection |

## First fit purchase

Buy **four each of M3 x 8, 10, 12, 14 and 18; four M3 x 50; four M3 locknuts; 30 ordinary 0.5 mm M3 washers; and 20 of the 1.0 mm metal spacer washers**. This covers a representative four-screw fit for every horn stack plus one clamp set. Reuse one servo's original centre screws. Quantities and lookup links are also in [fasteners.csv](../metadata/fasteners.csv).

Fit the drive and passive horns separately. Calibrate the printed spacers to the actual horn faces, measure washer thickness, check thread engagement and verify free movement with power disconnected. Check that the metal horns remain seated, the clamp captures the case without distortion, and fastener heads/nuts/tips do not touch adjacent parts. Tighten evenly with a hand driver; a generic steel-bolt torque table is not a suitable torque specification for thin aluminum horns and PLA clamps. A numerical assembly torque needs supplier guidance or a physical trial.

Tools: 2.5 mm hex driver for the selected M3 cap screws, a 5.5 mm nut driver/spanner, the driver matching the supplied servo centre screws, and calipers. A 2 mm hex driver suits the proposed M2.5 cap screws. Spare quantities are intentionally separate from CAD-required quantities.

## China sourcing and budget

The [佰瑞特 JD flagship store](https://mall.jd.com/index-84602.html) lists screws, washers, nuts and standoffs. It is a sourcing starting point, not a verified offer for every chosen length/material. Each table row links to exact search wording for JD and Taobao; these are **search links, not verified seller SKUs or live stock promises**. M3 x 14/18, long M3 bolts and the 1 mm washer dimensions need particular attention to the variant selector. Steel 8.8 is the preferred class; a same-size higher-class steel cap screw can be considered only with the same measured head/length and the same cautious tightening appropriate to PLA.

Reserve roughly **¥120–180 for fasteners**, as a planning allowance inside BOM item 11's ¥320 basic-structure allocation. This is not a current quote or an additional charge to the existing BOM total. Final quantities/cost will rise when the remaining attachment features are counted; the wider project revision reserve is available if needed.

CAD-derived per-joint allocation: [fastener_interfaces.csv](../metadata/fastener_interfaces.csv). Arithmetic/source fingerprint: [fastener_summary.json](../metadata/fastener_summary.json). The generator verifies counts and stack arithmetic; it does not check hardware collision or physical fit.
