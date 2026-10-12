# JammyFox — Simple Servo BOM

Updated: 2026-10-12 (Asia/Shanghai)  
Currency: RMB (CNY)  
Status: planning BOM with CAD Revision A; prices are allowances. The fastener supplement specifies hardware families and nominal joint stacks; remaining attachment details and physical fit are not released for manufacture.

## Scope

A 50 cm Minecraft-style fox with a PLA shell that walks, grasps small items with its mouth, shakes its head and swings its tail.

Use bus servos, servo bus control, battery/charging/power modules, onboard MPU/MCU and basic mechanical structure. The external Jetson Orin Nano Super 8 GB is already owned and runs the main inference. The RTX 5090 workstation is used for simulation, training and testing.

The initial tasks are slow walking on level ground, controlled head/tail movement and grasping an object positioned at the mouth by an operator. This BOM has no camera or external contact/attitude sensors. Simulation and any learned walking controller must use the observations available from the actual servo system.

Working size assumption: 50 cm nose to rump, excluding the moving tail. Printer and basic tools are already available.

## Servo allocation

| Assembly | Joints | Servo count |
|---|---|---:|
| Four legs | Hip sideways, hip forward/backward, knee on each leg | 12 |
| Neck | Yaw for shaking and pitch for mouth positioning | 2 |
| Mouth | One jaw opening/closing joint | 1 |
| Tail | One sideways swing joint | 1 |
| **Total** | **One common 12 V bus-servo model** | **16** |

Use the standard ST3215 family for all 16 joints. Final suitability depends on the finished mass, leg geometry and required mouth payload. Manufacturer stall torque is not a continuous working torque rating. [Manufacturer specification](https://www.waveshare.com/product/st3215-servo.htm), [Feetech 12 V model reference](https://www.feetechrc.com/products.html?keyword=STS3215)

## Parts and purchase links

Every amount below is a **budget allowance**, not a verified live seller quotation. “Qty 1” for a cable/material/structure lot is one budget allocation.

| ID | Part | Specification | Qty | Unit allowance (RMB) | Subtotal (RMB) | JD / Taobao links |
|---|---|---|---:|---:|---:|---|
| 01 | Bus servos / 总线舵机 | 16 × confirmed FEETECH ST-3215-C018, 12 V / 30 kg·cm; stock metal horns | 16 | 150 | 2400 | [Selected JD package](https://item.jd.com/10205990758166.html) · [JD search](https://search.jd.com/Search?keyword=%E9%A3%9E%E7%89%B9%20ST3215%20ST-3215-C018%2012V%2030KG&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=%E9%A3%9E%E7%89%B9%20ST3215%20ST-3215-C018%2012V%2030KG) |
| 02 | MPU base module / MPU基础模块 | Radxa ZERO 3W, target 2 GB + 32 GB microSD + small heatsink; confirm exact variant | 1 | 370 | 370 | [Item reference](https://item.taobao.com/item.htm?id=763812025816) · [JD search](https://search.jd.com/Search?keyword=%E7%91%9E%E8%8E%8E%20Radxa%20ZERO%203W%202GB&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=%E7%91%9E%E8%8E%8E%20Radxa%20ZERO%203W%202GB) |
| 03 | MCU + servo bus controller / MCU总线控制板 | Waveshare Servo Driver with ESP32, SKU 21593; TTL ST-series servo interface included | 1 | 120 | 120 | [Item reference](https://item.jd.com/10228911103849.html) · [JD search](https://search.jd.com/Search?keyword=%E5%BE%AE%E9%9B%AA%20Servo%20Driver%20with%20ESP32%2021593&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=%E5%BE%AE%E9%9B%AA%20Servo%20Driver%20with%20ESP32%2021593) |
| 04 | Bus and data cables / 总线及数据线 | ST3215 3-pin cables, short MPU–MCU USB data cable, and branch connection supplies; final lengths/counts after layout | 1 | 50 | 50 | [JD search](https://search.jd.com/Search?keyword=ST3215%205264%203P%20%E8%88%B5%E6%9C%BA%E7%BA%BF%20USB%20%E6%95%B0%E6%8D%AE%E7%BA%BF&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=ST3215%205264%203P%20%E8%88%B5%E6%9C%BA%E7%BA%BF%20USB%20%E6%95%B0%E6%8D%AE%E7%BA%BF) |
| 05 | Battery / 电池 | Gens Ace/格氏 3S LiPo, 2200 mAh, XT60; discharge capability to confirm | 1 | 150 | 150 | [Item reference](https://item.jd.com/100109571439.html) · [JD search](https://search.jd.com/Search?keyword=%E6%A0%BC%E6%B0%8F%202200mAh%203S%2011.1V%20XT60%2030C&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=%E6%A0%BC%E6%B0%8F%202200mAh%203S%2011.1V%20XT60%2030C) |
| 06 | Balance charger / 平衡充电器 | Genuine SkyRC B6neo SK-100198; correct 3S main/balance leads included in selected package | 1 | 180 | 180 | [JD search](https://search.jd.com/Search?keyword=%E5%A4%A9%E7%A9%BA%E5%88%9B%E6%96%B0%20SKYRC%20B6neo%20SK-100198&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=%E5%A4%A9%E7%A9%BA%E5%88%9B%E6%96%B0%20SKYRC%20B6neo%20SK-100198) |
| 07 | Charger power supply / 充电器电源 | Compatible USB-C PD supply and cable, approximately 65 W target | 1 | 60 | 60 | [JD search](https://search.jd.com/Search?keyword=USB%20PD%2065W%2020V%20%E7%94%B5%E6%BA%90%20%E7%BA%BF&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=USB%20PD%2065W%2020V%20%E7%94%B5%E6%BA%90%20%E7%BA%BF) |
| 08 | 5 V power module / 5V电源模块 | 3S input to regulated 5 V; at least 3 A continuous target for onboard logic | 1 | 40 | 40 | [JD search](https://search.jd.com/Search?keyword=DC%20DC%20%E9%99%8D%E5%8E%8B%205V%203A%2012V%20%E6%A8%A1%E5%9D%97&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=DC%20DC%20%E9%99%8D%E5%8E%8B%205V%203A%2012V%20%E6%A8%A1%E5%9D%97) |
| 09 | Power distribution / 配电基础模块 | Battery connector, separately rated servo branches, wiring, fuse and actuator power cutoff; final ratings after load estimate | 1 | 110 | 110 | [JD search](https://search.jd.com/Search?keyword=XT60%20%E9%85%8D%E7%94%B5%E6%9D%BF%20%E7%A1%85%E8%83%B6%E7%BA%BF%20%E4%BF%9D%E9%99%A9%E4%B8%9D%20%E7%94%B5%E6%BA%90%E5%BC%80%E5%85%B3&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=XT60%20%E9%85%8D%E7%94%B5%E6%9D%BF%20%E7%A1%85%E8%83%B6%E7%BA%BF%20%E4%BF%9D%E9%99%A9%E4%B8%9D%20%E7%94%B5%E6%BA%90%E5%BC%80%E5%85%B3) |
| 10 | PLA body / PLA机体 | PLA for shell, rigid feet, jaw and lightweight hollow tail; orange/white/black material allowance | 1 | 120 | 120 | [JD search](https://search.jd.com/Search?keyword=PLA%20%E8%80%97%E6%9D%90%201.75%20%E6%A9%99%E8%89%B2%20%E7%99%BD%E8%89%B2%20%E9%BB%91%E8%89%B2&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=PLA%20%E8%80%97%E6%9D%90%201.75%20%E6%A9%99%E8%89%B2%20%E7%99%BD%E8%89%B2%20%E9%BB%91%E8%89%B2) |
| 11 | Basic structure / 基础结构件 | Stock C018 metal horns, printed clamps/brackets, 2 mm aluminum chassis, M3 socket-head screws/nuts/washers and proposed M2.5 PCB hardware; see [fastener schedule](FASTENERS.md) | 1 | 320 | 320 | [JD hardware store](https://mall.jd.com/index-84602.html) · [JD search](https://search.jd.com/Search?keyword=8.8%20%E9%95%80%E9%94%8C%20DIN912%20M3%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20%E8%9E%BA%E4%B8%9D&enc=utf-8) · [Taobao search](https://s.taobao.com/search?q=8.8%20%E9%95%80%E9%94%8C%20DIN912%20M3%20%E6%9D%AF%E5%A4%B4%E5%86%85%E5%85%AD%E8%A7%92%20%E8%9E%BA%E4%B8%9D) |

## Budget

| Item | Allowance (RMB) |
|---|---:|
| 16 servos | 2400 |
| MPU, MCU/controller and cables | 540 |
| Battery, charger, supplies and power distribution | 540 |
| PLA and basic structure | 440 |
| **Core parts allowance** | **3920** |
| Shipping, spare parts and revisions | 400 |
| **Total planning allowance** | **4320** |

The remaining budget is ¥4,000–5,400. This version targets ¥4,320, leaving ¥1,080 below the upper limit. The total includes a ¥400 reserve; revise it against actual delivered prices before procurement.

The already owned Jetson, workstation, printer and tools are excluded. A new Wi-Fi router is not listed: use an existing wireless LAN or a supported Jetson hotspot.

Fasteners use a planning allowance of ¥120–180 **within item 11**, not in addition to it. [FASTENERS.md](FASTENERS.md) and [fasteners.csv](../metadata/fasteners.csv) provide nominal quantities, sample-purchase quantities and JD/Taobao search links. The 120 horn screws and 64 clamp bolt positions are CAD-derived; remaining frame/cover attachment hardware needs further detailing, so this is not yet the complete assembly fastener cost.

## Simple control arrangement

```text
RTX 5090 workstation <-- Wi-Fi LAN --> external Jetson
                                            |
                                         Wi-Fi LAN
                                            |
                                  onboard ZERO 3W MPU
                                            |
                                    short USB data link
                                            |
                               ESP32 MCU / TTL servo bus
                                            |
                                      16 bus servos
```

The servos supply their built-in position control and available bus feedback. The MCU coordinates servo commands and command expiry; the MPU handles wireless communication and local motion sequences. Target approximately 50 Hz command updates initially and measure actual bus timing. No separate high-rate torque-control hardware is assumed.

Walking contacts are inferred by the controller if needed; there are no foot switches. Head shaking and tail swinging use bounded position trajectories. Mouth grasping uses a known jaw opening and bounded closure command; available servo load feedback can assist after validation, but it is not a calibrated jaw-force sensor. Camera-based object finding is outside this version's hardware scope.

## Essential compatibility details

- **One voltage family:** specify the 12 V ST3215 variant for every servo. A 3S battery is 11.1 V nominal and 12.6 V full; confirm the selected controller revision and its power wiring support the full battery voltage.
- **Separate motor power branches:** Waveshare states a 5 A maximum for the ESP32 servo driver board. The power module must feed the multi-servo system through separately rated branches. Do not pass all servo current through the controller board. [Manufacturer power instructions](https://docs.waveshare.net/Servo_Driver_with_ESP32/Product-Use/)
- **Correct bus interface:** the listed controller supports TTL ST-series bus servos and needs the matching firmware. A PWM-only controller is not compatible. [Controller documentation](https://docs.waveshare.net/Servo_Driver_with_ESP32/)
- **Wireless MPU:** buy ZERO 3W with the intended RAM/storage/antenna configuration. Verify the supported Linux image and USB cable connectors. [Radxa documentation](https://docs.radxa.com/en/zero/zero3)
- **Charging accessories:** the B6neo requires a compatible external power supply and correct main/balance leads. Both are covered by the allowances above. [SkyRC documentation](https://www.skyrc.com/cn/b6neo-series)
- **Basic structure:** rigid PLA body parts and ordinary brackets/bearings/fasteners are the mechanical plan. There are no dedicated soft-material assemblies. Keep the head and hollow PLA tail light; their final joint loads must be included in servo sizing.

## Purchase-link status

Links were researched on 2026-10-12.

| Link type | Meaning |
|---|---|
| Item reference | Specific JD/Taobao listing identified during research; current price, stock and exact variant unconfirmed |
| JD search / Taobao search | Keyword search link for selecting an appropriate offer; not a confirmed seller quotation |

The direct references were identified through the [JD servo catalog](https://www.jd.com/jiage/652a98aa4c00f38704b.html), [JD controller catalog](https://www.jd.com/xinghao/9855b16f3a109bd9c50b.html), [JD battery catalog](https://www.jd.com/jiage/623354860cce65899096.html) and a [published ZERO 3W reference BOM](https://github.com/fanhao375/microduck-replica-cad). Several direct pages could not be read because of marketplace access restrictions; use the labeled search alternatives to confirm the exact package and delivered price.

Digital CAD Revision A is available in [mechanical notes](MECHANICAL.md). Physical parts and firmware have not been built. MuJoCo models are included in [mjcf](../mjcf/README.md). The CAD mass estimate is higher than the early target, and fit/load validation remains necessary before manufacture.
