# The Air Gap Is a Myth: Why Passive Monitoring Matters

In industrial environments, it's common to hear,  
> “We're safe — our systems are air-gapped.”

But in the real world, **true air gaps are rare**, and the illusion of isolation can be dangerous.

---

## 🧠 Why the Air Gap Isn’t What It Seems

Most OT networks today:

- Allow **remote vendor access** via tools like TeamViewer or AnyDesk — often insecure and unmonitored  
- Use **VPNs** that traverse both IT and OT segments without proper segmentation  
- Share connectivity with corporate IT networks (e.g., Active Directory, email alerts)  
- Are bridged by **USB drives**, **misconfigured firewalls**, or **dual-homed devices**  
- Include **cloud-connected sensors**, smart HMIs, or telemetry pushing to third parties  
- Suffer from **poor IT hygiene by operators**, including:
  - Using workstations for personal browsing or media
  - Leaving devices unlocked or unattended
  - Reusing passwords or sharing credentials  
  - Bringing in personal USB drives or peripherals

Even "offline" environments can become **temporarily exposed** during diagnostics, firmware updates, or vendor troubleshooting — often with no logging or alerting in place.

---

## 💣 Historical Evidence

- **Stuxnet** spread across isolated networks via USB and Windows zero-days, proving that air gaps can be crossed.
- **TRITON/Trisis** compromised safety instrumented systems in what was assumed to be a segmented plant environment.
- **U.S. Water Utilities** have been publicly called out in reports for having exposed endpoints despite "offline" claims.

---

## 🛡️ Why Passive Monitoring Is Essential

Even if you believe your system is segmented, **you can't defend what you can't see**.

LineAlert provides:
- **Visibility into field-level device behavior**
- A **non-invasive safety net** that runs on low-cost hardware
- A way to **detect unexpected protocol usage, new function codes, or behavioral drift**
- Peace of mind for environments with no existing IDS/monitoring stack

---

## 🌱 Our Philosophy

We're not trying to replace your firewall or SOC.

We're here to **give the under-resourced ops guy, public safety team, or small-town technician a fighting chance** to spot trouble before it spreads.

Passive, low-cost monitoring is not an alternative to segmentation — it's the **reality check** that makes segmentation meaningful.

---

> Want to help validate or improve this doc? Submit a PR or share real-world stories where segmentation failed — we’ll anonymize and amplify.
