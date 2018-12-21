%define orig_name intel-microcode
%define orig_timestamp 20180807
%define orig_rev a

Name: firmware-intel-ucode
Version: 7
Release: alt1.%{orig_timestamp}%{?orig_rev:.%orig_rev}
Epoch: 2

Packager: L.A. Kostis <lakostis@altlinux.org>

Summary: Microcode definitions for Intel processors
License: INTEL SOFTWARE LICENSE AGREEMENT
Group: System/Kernel and hardware
Provides: microcode-data-intel = %version-%release
Obsoletes: microcode-data-intel <= 20130222-alt2

URL: https://anonscm.debian.org/cgit/users/hmh/intel-microcode.git/
Source0: %{orig_name}-%{orig_timestamp}%{orig_rev}.tar

BuildRequires: iucode_tool

# beware that this probably should be ix86
# but who cares about intel on ARM?
BuildArch: noarch
ExclusiveArch: %ix86 x86_64

%description
The microcode data file for Linux contains the latest microcode
definitions for all Intel processors.

%prep
%setup -q -n %orig_name-%{orig_timestamp}%{orig_rev}

%build
%make_build

%install
mkdir -p %buildroot/lib/firmware/intel-ucode
UCODE=intel-microcode
%ifarch %ix86
# use stripped down version for x86_64 and ia32
UCODE=${UCODE}-64
%endif
mv ${UCODE}.bin %buildroot/lib/firmware/intel-ucode/%{orig_name}.bin

%files
%doc changelog releasenote
%dir /lib/firmware/intel-ucode
/lib/firmware/intel-ucode/*

%changelog
* Thu Aug 30 2018 L.A. Kostis <lakostis@altlinux.ru> 2:7-alt1.20180807.a
- Sync with Debian 3.20180807a1:
  + New Microcodes:
    sig 0x000206c2, pf_mask 0x03, 2018-05-08, rev 0x001f, size 11264
    sig 0x000206e6, pf_mask 0x04, 2018-05-15, rev 0x000d, size 9216
    sig 0x000506c2, pf_mask 0x01, 2018-05-11, rev 0x0014, size 15360
    sig 0x000506ca, pf_mask 0x03, 2018-05-11, rev 0x000c, size 14336
    sig 0x000506f1, pf_mask 0x01, 2018-05-11, rev 0x0024, size 10240
  + Updated Microcodes:
    sig 0x000106a5, pf_mask 0x03, 2018-05-11, rev 0x001d, size 12288
    sig 0x000106e5, pf_mask 0x13, 2018-05-08, rev 0x000a, size 9216
    sig 0x00020652, pf_mask 0x12, 2018-05-08, rev 0x0011, size 9216
    sig 0x00020655, pf_mask 0x92, 2018-04-23, rev 0x0007, size 4096
    sig 0x000206a7, pf_mask 0x12, 2018-04-10, rev 0x002e, size 12288
    sig 0x000206f2, pf_mask 0x05, 2018-05-16, rev 0x003b, size 14336
    sig 0x000306a9, pf_mask 0x12, 2018-04-10, rev 0x0020, size 13312
    sig 0x000306c3, pf_mask 0x32, 2018-04-02, rev 0x0025, size 23552
    sig 0x000306d4, pf_mask 0xc0, 2018-03-22, rev 0x002b, size 18432
    sig 0x00040651, pf_mask 0x72, 2018-04-02, rev 0x0024, size 22528
    sig 0x00040661, pf_mask 0x32, 2018-04-02, rev 0x001a, size 25600
    sig 0x00040671, pf_mask 0x22, 2018-04-03, rev 0x001e, size 13312
    sig 0x000406e3, pf_mask 0xc0, 2018-04-17, rev 0x00c6, size 99328
    sig 0x00050662, pf_mask 0x10, 2018-05-25, rev 0x0017, size 31744
    sig 0x00050663, pf_mask 0x10, 2018-04-20, rev 0x7000013, size 22528
    sig 0x00050664, pf_mask 0x10, 2018-04-20, rev 0xf000012, size 22528
    sig 0x000506c9, pf_mask 0x03, 2018-05-11, rev 0x0032, size 16384
    sig 0x000506e3, pf_mask 0x36, 2018-04-17, rev 0x00c6, size 99328
    sig 0x000706a1, pf_mask 0x01, 2018-05-22, rev 0x0028, size 73728
    sig 0x000806e9, pf_mask 0xc0, 2018-03-24, rev 0x008e, size 98304
    sig 0x000806ea, pf_mask 0xc0, 2018-05-15, rev 0x0096, size 98304
    sig 0x000906e9, pf_mask 0x2a, 2018-03-24, rev 0x008e, size 98304
    sig 0x000906ea, pf_mask 0x22, 2018-05-02, rev 0x0096, size 97280
    sig 0x000906eb, pf_mask 0x02, 2018-03-24, rev 0x008e, size 98304
  + Implements L1D_FLUSH support (L1TF "Foreshadow/-NG" mitigation)
    Intel SA-00161, CVE-2018-3615, CVE-2018-3620, CVE-2018-3646
  + Implements SSBD support (Spectre v4 mitigation),
    Disable speculation for (some) RDMSR/WRMSR (Spectre v3a fix)
    Intel SA-00115, CVE-2018-3639, CVE-2018-3640
  + Implements IBRS/IBPB/STIPB support, Spectre v2 mitigation for older
    processors with signatures 0x106a5, 0x106e5, 0x20652, 0x20655.
    Intel SA-0088, CVE-2017-5753, CVE-2017-5754
  - source: update symlinks to reflect id of the latest release, 20180807a

* Mon Aug 06 2018 L.A. Kostis <lakostis@altlinux.ru> 2:6-alt1.20180703
- Sync with Debian 3.20180703.2:
  + Updated Microcodes:
      sig 0x000206d6, pf_mask 0x6d, 2018-05-08, rev 0x061d, size 18432
      sig 0x000206d7, pf_mask 0x6d, 2018-05-08, rev 0x0714, size 19456
      sig 0x000306e4, pf_mask 0xed, 2018-04-25, rev 0x042d, size 15360
      sig 0x000306e7, pf_mask 0xed, 2018-04-25, rev 0x0714, size 17408
      sig 0x000306f2, pf_mask 0x6f, 2018-04-20, rev 0x003d, size 33792
      sig 0x000306f4, pf_mask 0x80, 2018-04-20, rev 0x0012, size 17408
      sig 0x000406f1, pf_mask 0xef, 2018-04-19, rev 0xb00002e, size 28672
      sig 0x00050654, pf_mask 0xb7, 2018-05-15, rev 0x200004d, size 31744
      sig 0x00050665, pf_mask 0x10, 2018-04-20, rev 0xe00000a, size 18432
  + First batch of fixes for: Intel SA-00115, CVE-2018-3639, CVE-2018-3640
  + SSBD support (Spectre-v4 mitigation) and fix Spectre-v3a for:
      Sandybridge server, Ivy Bridge server, Haswell server, Skylake server,
      Broadwell server, a few HEDT Core i7/i9 models that are actually gimped
      server dies.
  - source: update symlinks to reflect id of the latest release, 20180703

* Mon Jun 18 2018 L.A. Kostis <lakostis@altlinux.ru> 2:5-alt2.20180425
- Make package %%ix86/x86_64 only.

* Mon Jun 18 2018 L.A. Kostis <lakostis@altlinux.ru> 2:5-alt1.20180425
- Update 20180425 (debian changelog below):
  + Updated Microcodes:
    sig 0x000406f1, pf_mask 0xef, 2018-03-21, rev 0xb00002c, size 27648
    sig 0x000706a1, pf_mask 0x01, 2017-12-26, rev 0x0022, size 73728
  + Implements IBRS/IBPB/STIPB support, Spectre-v2 mitigation
  - source: remove undesired list files from microcode directories
  - source: switch to microcode-<id>.d/ since Intel dropped .dat
    support.

* Tue Mar 20 2018 L.A. Kostis <lakostis@altlinux.ru> 2:4-alt1.20180312
- Update to 20180312.
  + New Microcodes:
    sig 0x00050653, pf_mask 0x97, 2018-01-29, rev 0x1000140, size 30720
    sig 0x00050665, pf_mask 0x10, 2018-01-22, rev 0xe000009, size 18432
  + Updated Microcodes:
    sig 0x000206a7, pf_mask 0x12, 2018-02-07, rev 0x002d, size 12288
    sig 0x000206d6, pf_mask 0x6d, 2018-01-30, rev 0x061c, size 18432
    sig 0x000206d7, pf_mask 0x6d, 2018-01-26, rev 0x0713, size 19456
    sig 0x000306a9, pf_mask 0x12, 2018-02-07, rev 0x001f, size 13312
    sig 0x000306c3, pf_mask 0x32, 2018-01-21, rev 0x0024, size 23552
    sig 0x000306d4, pf_mask 0xc0, 2018-01-18, rev 0x002a, size 18432
    sig 0x000306e4, pf_mask 0xed, 2018-01-25, rev 0x042c, size 15360
    sig 0x000306e7, pf_mask 0xed, 2018-02-16, rev 0x0713, size 16384
    sig 0x000306f2, pf_mask 0x6f, 2018-01-19, rev 0x003c, size 33792
    sig 0x000306f4, pf_mask 0x80, 2018-01-22, rev 0x0011, size 17408
    sig 0x00040651, pf_mask 0x72, 2018-01-18, rev 0x0023, size 21504
    sig 0x00040661, pf_mask 0x32, 2018-01-21, rev 0x0019, size 25600
    sig 0x00040671, pf_mask 0x22, 2018-01-21, rev 0x001d, size 12288
    sig 0x000406e3, pf_mask 0xc0, 2017-11-16, rev 0x00c2, size 99328
    sig 0x00050654, pf_mask 0xb7, 2018-01-26, rev 0x2000043, size 28672
    sig 0x00050662, pf_mask 0x10, 2018-01-22, rev 0x0015, size 31744
    sig 0x00050663, pf_mask 0x10, 2018-01-22, rev 0x7000012, size 22528
    sig 0x00050664, pf_mask 0x10, 2018-01-22, rev 0xf000011, size 22528
    sig 0x000506c9, pf_mask 0x03, 2017-03-25, rev 0x002c, size 16384
    sig 0x000506e3, pf_mask 0x36, 2017-11-16, rev 0x00c2, size 99328
    sig 0x000706a1, pf_mask 0x01, 2017-10-31, rev 0x001e, size 72704
    sig 0x000806e9, pf_mask 0xc0, 2018-01-21, rev 0x0084, size 98304
    sig 0x000806ea, pf_mask 0xc0, 2018-01-21, rev 0x0084, size 97280
    sig 0x000906e9, pf_mask 0x2a, 2018-01-21, rev 0x0084, size 98304
    sig 0x000906ea, pf_mask 0x22, 2018-01-21, rev 0x0084, size 96256
    sig 0x000906eb, pf_mask 0x02, 2018-01-21, rev 0x0084, size 98304

* Thu Feb 08 2018 Konstantin A. Lepikhov <lakostis@altlinux.ru> 2:3-alt3.20171117
- Rollback microcode files back to 20171117 (debian changelog below):
  + Revert to release 20171117, as per Intel instructions issued to
    the public in 2018-01-22 (closes: #886998)
  + This effectively removes IBRS/IBPB/STIPB microcode support for
    Spectre variant 2 mitigation.

* Wed Jan 10 2018 L.A. Kostis <lakostis@altlinux.ru> 2:3-alt2.20180108
- bump epoch (again) and restore old versioning.
- removed external microcode files:
  + sig 0x000306f2, pf_mask 0x6f, 2017-11-17, rev 0x003b (merged)
  + sig 0x000406f1, pf_mask 0xef, 2017-11-18, rev 0xb000025 (downgraded)
  + sig 0x00050654, pf_mask 0xb7, 2017-11-21, rev 0x200003a (obsoleted).

* Wed Jan 10 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:3.20180108-alt1
- Update to 20180108 (adapted debian changelog is below):
  * New upstream microcode data file 20180108
    + Updated Microcodes:
      sig 0x000306c3, pf_mask 0x32, 2017-11-20, rev 0x0023, size 23552
      sig 0x000306d4, pf_mask 0xc0, 2017-11-17, rev 0x0028, size 18432
      sig 0x000306e4, pf_mask 0xed, 2017-12-01, rev 0x042a, size 15360
      sig 0x000306f2, pf_mask 0x6f, 2017-11-17, rev 0x003b, size 33792
      sig 0x000306f4, pf_mask 0x80, 2017-11-17, rev 0x0010, size 17408
      sig 0x00040651, pf_mask 0x72, 2017-11-20, rev 0x0021, size 22528
      sig 0x00040661, pf_mask 0x32, 2017-11-20, rev 0x0018, size 25600
      sig 0x00040671, pf_mask 0x22, 2017-11-17, rev 0x001b, size 13312
      sig 0x000406e3, pf_mask 0xc0, 2017-11-16, rev 0x00c2, size 99328
      sig 0x00050654, pf_mask 0xb7, 2017-12-08, rev 0x200003c, size 27648
      sig 0x00050662, pf_mask 0x10, 2017-12-16, rev 0x0014, size 31744
      sig 0x00050663, pf_mask 0x10, 2017-12-16, rev 0x7000011, size 22528
      sig 0x000506e3, pf_mask 0x36, 2017-11-16, rev 0x00c2, size 99328
      sig 0x000706a1, pf_mask 0x01, 2017-12-26, rev 0x0022, size 73728
      sig 0x000806e9, pf_mask 0xc0, 2018-01-04, rev 0x0080, size 98304
      sig 0x000806ea, pf_mask 0xc0, 2018-01-04, rev 0x0080, size 98304
      sig 0x000906e9, pf_mask 0x2a, 2018-01-04, rev 0x0080, size 98304
      sig 0x000906ea, pf_mask 0x22, 2018-01-04, rev 0x0080, size 97280
      sig 0x000906eb, pf_mask 0x02, 2018-01-04, rev 0x0080, size 98304
    + Implements IBRS/IBPB support and enhances LFENCE: mitigation
      against Spectre (fixes CVE-2017-5715)
    + Very likely fixes several other errata on some of the processors
  * supplementary-ucode-CVE-2017-5715.d/: remove.
    + Downgraded microcodes:
      sig 0x000406f1, pf_mask 0xef, 2017-03-01, rev 0xb000021, size 26624
      sig 0x000506c9, pf_mask 0x03, 2017-03-25, rev 0x002c, size 16384
    + This removes IBRS/IBPB support for these two platforms when compared
      with the previous (and unofficial) release, 20171215.  We don't know
      why Intel declined to include these microcode updates (as well as
      several others) in the release.
  * source: remove superseded upstream data file: 20171117

* Thu Jan 04 2018 L.A. Kostis <lakostis@altlinux.ru> 1:3-alt1.20171121
- Added new CPU microcodes (microcode counterpart of the CVE-2017-5715
  kernel mitigation):
  + sig 0x000306f2, pf_mask 0x6f, 2017-11-17, rev 0x003b, size 33792
  + sig 0x000406f1, pf_mask 0xef, 2017-11-18, rev 0xb000025, size 27648
  + sig 0x00050654, pf_mask 0xb7, 2017-11-21, rev 0x200003a, size 27648

* Fri Nov 24 2017 L.A. Kostis <lakostis@altlinux.ru> 1:3-alt0.20171117.1
- Update to 20171117.1 (debian changelog below):
  * New upstream microcode data file 20171117
    + New Microcodes:
      sig 0x000506c9, pf_mask 0x03, 2017-03-25, rev 0x002c, size 16384
      sig 0x000706a1, pf_mask 0x01, 2017-10-31, rev 0x001e, size 72704
      sig 0x000906ea, pf_mask 0x22, 2017-08-23, rev 0x0070, size 95232
      sig 0x000906eb, pf_mask 0x02, 2017-09-20, rev 0x0072, size 97280
    + Updated Microcodes:
      sig 0x00050654, pf_mask 0xb7, 2017-10-17, rev 0x2000035, size 26624
      sig 0x000806ea, pf_mask 0xc0, 2017-08-03, rev 0x0070, size 96256
  * source: remove superseded upstream data file: 20170707.
  * source: remove unneeded intel-ucode/ directory for 20171117.
- TODO: we need to implement ucode blacklisting as well as debian does.


* Mon Sep 04 2017 L.A. Kostis <lakostis@altlinux.ru> 1:3-alt0.20170707.1
- Rebased to Debian package (because Fedora version is outdated):
  * New upstream microcode datafile 20170707
    + New Microcodes:
      sig 0x00050654, pf_mask 0x97, 2017-06-01, rev 0x2000022, size 25600
      sig 0x000806e9, pf_mask 0xc0, 2017-04-27, rev 0x0062, size 97280
      sig 0x000806ea, pf_mask 0xc0, 2017-05-23, rev 0x0066, size 95232
      sig 0x000906e9, pf_mask 0x2a, 2017-04-06, rev 0x005e, size 97280
    + This release fixes the nightmare-level errata SKZ7/SKW144/SKL150/
      SKX150 (Skylake) KBL095/KBW095 (Kaby Lake) for all affected Kaby
      Lake and Skylake processors: Skylake D0/R0 were fixed since the
      previous upstream release (20170511).  This new release adds the
      fixes for Kaby Lake Y0/B0/H0 and Skylake H0 (Skylake-E/X).
    + Fix undisclosed errata in Skylake H0 (0x50654), Kaby Lake Y0
      (0x806ea), Kaby Lake H0 (0x806e9), Kaby Lake B0 (0x906e9)
  * source: remove unneeded intel-ucode/ directory
  * source: remove superseded upstream data file: 20170511

* Thu Dec 08 2016 L.A. Kostis <lakostis@altlinux.ru> 1:2.1-alt0.3
- Updated to 2.1-11 version:
  + Intel CPU microcode 20161104 update.

* Wed Jun 08 2016 L.A. Kostis <lakostis@altlinux.ru> 1:2.1-alt0.2
- Updated to 2.1-8 version:
  + Intel CPU microcode 20151106 update.

* Mon Aug 12 2013 L.A. Kostis <lakostis@altlinux.ru> 1:2.1-alt0.1
- 2.1.
- remove amd-ucode (now part of linux-firmware).

* Mon Apr 08 2013 L.A. Kostis <lakostis@altlinux.ru> 1:2.0-alt0.2
- Get rid of versioning mess.

* Mon Apr 08 2013 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt0.1
- 2.0 release from fedora.
- it's just a helper for seamless in-kernel firmware management.
- combine separate firmware files.

* Tue Nov 09 2010 Victor Forsiuk <force@altlinux.org> 1.17-alt2
- Package only utility. Microcode data will be in separate packages.
- Move utility from %_sbindir to /sbin.
- Use /lib/microcode for microcode data instead of /etc.

* Wed May 02 2007 Victor Forsyuk <force@altlinux.org> 1.17-alt1
- 1.17

* Mon Apr 02 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt2
- Comment ExclusiveArch for now.

* Tue Mar 27 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt1
- 1.16

* Mon Nov 13 2006 Denis Smirnov <mithraen@altlinux.ru> 1.14-alt1
- Update to 1.14

* Mon Dec 12 2005 Victor Forsyuk <force@altlinux.ru> 1.12-alt2
- Shift service start priority to run after udev is up.
- Remove microcode kernel module after microcode uploading.

* Wed Oct 19 2005 Victor Forsyuk <force@altlinux.ru> 1.12-alt1
- Initial build.
