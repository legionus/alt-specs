%define	systemdsystemunitdir	/lib/systemd/system
%define	firmwaredir		/lib/firmware

Name: libudev0
Version: 181
Release: alt7
Summary: Shared library to access udev device information
License: LGPLv2.1+
Group: System/Legacy libraries
Url: http://kernel.org/pub/linux/utils/kernel/hotplug/

Provides: libudev = %version-%release
Obsoletes: libudev < %version-%release

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: glib2-devel gobject-introspection-devel gperf gtk-doc pciids usbids
BuildRequires: libacl-devel libusb-compat-devel usbutils libselinux-devel
BuildRequires: kmod-devel >= 5 libblkid-devel >= 2.20

%description
This package provides shared library to access udev device information

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--enable-floppy \
	--enable-edd \
	--enable-udev_acl \
	--enable-rule_generator \
	--enable-introspection \
	--with-selinux \
	--disable-gudev \
	--disable-introspection \
	--sbindir=/sbin \
	--bindir=/sbin \
	--libexecdir=/lib \
	--with-rootlibdir=/%_lib \
	--with-firmware-path=%firmwaredir/updates:%firmwaredir \
	--with-systemdsystemunitdir=%systemdsystemunitdir \
	--with-usb-ids-path=/usr/share/misc/usb.ids \
	--disable-silent-rules
%make_build

%install
%makeinstall_std

%files
/%_lib/libudev.so.*

%changelog
* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 181-alt7
- Fixed build.

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 181-alt6
- build to sisyphus

* Mon Jul 02 2012 Dmitry V. Levin <ldv@altlinux.org> 181-alt5
- Added an "Obsoletes" tag (closes: #27448).

* Wed Jun 20 2012 Alexey Shabalin <shaba@altlinux.ru> 181-alt4
- add Provides: libudev

* Wed Jun 13 2012 Alexey Shabalin <shaba@altlinux.ru> 181-alt3
- build as legacy libraries "libudev0" for compat

* Mon May 28 2012 Dmitry V. Levin <ldv@altlinux.org> 181-alt2
- Reintroduced udev-rule-generator package and udevd-final startup
  script by reverting commit 180-alt1~4-g289489b which was erroneously
  pushed to Sisyphus few days ago.

* Fri Feb 10 2012 Valery Inozemtsev <shrek@altlinux.ru> 181-alt1
- 181

* Mon Jan 30 2012 Valery Inozemtsev <shrek@altlinux.ru> 180-alt1
- 180

* Fri Nov 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 175-alt1
- 175

* Thu Oct 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 174-alt1
- 174

* Wed Aug 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 173-alt1
- 173

* Mon Jul 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 172-alt2
- udev-rules: added provides /lib/udev/rules.d

* Mon Jul 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 172-alt1
- 172

* Fri May 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 171-alt1
- 171

* Fri May 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 170-alt1
- 170

* Thu May 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 169-alt1
- 169

* Thu May 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 168-alt2
- removed /lib/udev/devices/loop[0-3] (requires losetup >= 2.19.1)
- added conflicts to systemd < 25 (closes: #25552)

* Tue Apr 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 168-alt1
- 168

* Fri Apr 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 167-alt2
- initscripts: mount /run on tmpfs if directory exists
- added loop[0-3]

* Wed Mar 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 167-alt1
- 167
- initscripts: removed create_static_inodes

* Thu Feb 10 2011 Valery Inozemtsev <shrek@altlinux.ru> 166-alt1
- 166

* Tue Feb 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 165-alt2
- add systemd service files (closes: #24990)

* Thu Dec 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 165-alt1
- 165

* Sun Nov 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 164-alt2
- initscript:
  + fixed mount shm/pts filesystems
  + removed unused /etc/udev/devices

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 164-alt1
- 164

* Thu Oct 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 163-alt1
- 163

* Sat Sep 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 162-alt4
- udev-extras: required pciids, usbids

* Sun Sep 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 162-alt3
- set SELinux context after mounting tmpfs on /dev (by Mikhail Efremov)

* Fri Sep 17 2010 Dmitry V. Levin <ldv@altlinux.org> 162-alt2
- Fixed SELinux context setting for the static nodes (by Mikhail Efremov).
  This fixes regression introduced by faulty merge 161-alt2.
  The original change made in 150-alt9 was correct,
  the bug was introduced by that buggy merge.
- Merged some minor specfile fixes from 150-alt9.

* Sat Sep 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 162-alt1
- 162
- initscripts: added devtmpfs support

* Sat Aug 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 161-alt2
- added and enabled SELinux support (by Mikhail Efremov and Dmitry V. Levin)

* Wed Aug 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 161-alt1
- 161

* Sun Jul 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 160-alt1
- new upstream release (160)

* Wed Jul 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 159-alt1
- new upstream release (159)

* Thu Jun 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 158-alt1
- new upstream release (158)

* Wed Jun 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 157-alt1
- new upstream release (157)

* Tue May 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 156-alt1
- new upstream release (156)

* Tue May 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 155-alt1
- new upstream release (155)

* Wed May 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 154-alt2
- postrelease fises

* Wed May 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 154-alt1
- new upstream release (154)
- removed rule for compatibility with kernels 2.6.31 below

* Wed Apr 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 153-alt1
- new upstream release (153)

* Tue Apr 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 152-alt1
- new upstream release (152)

* Sun Apr 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 151-alt4
- rebuild

* Mon Mar 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 151-alt3
- udev-final: check for rules.d/ writeability (Michael Shigorin)
- device-mapper want property STARTUP to be set to 1 on coldplug (Kirill A. Shutemov)

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 151-alt2
- removed net-agent

* Wed Jan 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 151-alt1
- new upstream release (151)

* Sun Jan 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 150-alt2
- removed klibc support
- removed udev-initramfs subpackage

* Thu Jan 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 150-alt1
- new upstream release (150)

* Tue Dec 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 149-alt2
- firmware.c: upstream version

* Thu Dec 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 149-alt1
- new upstream release (149)

* Wed Dec 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 148-alt1
- new upstream release (148)

* Fri Nov 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 147-alt3
- udev-acl: migrated to ConsoleKit 0.4.1

* Mon Nov 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 147-alt2
- new libgudev-gir{,-devel} subpackages

* Tue Nov 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 147-alt1
- New upstream release (147)

* Tue Nov 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 146-alt4
- rebuild with latest klibc

* Sun Sep 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 146-alt3
- make raw USB printer devices accessible for lp

* Mon Aug 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 146-alt2
- gudev: build introspection library

* Fri Aug 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 146-alt1
- New upstream release (146)

* Tue Jul 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 145-alt1
- New upstream release (145)

* Thu Jul 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 141-alt9
- packaged libudev.a

* Fri Jun 19 2009 Dmitry V. Levin <ldv@altlinux.org> 141-alt8
- udevd-final (start): Append tmp rules instead of replacing.

* Thu Jun 18 2009 Dmitry V. Levin <ldv@altlinux.org> 141-alt7
- udevd-final (start): Move tmp rules
  from /dev/.udev/ to /etc/udev/rules.d/.
- 75-persistent-net-generator.rules: Allow to use
  "locally administered" MAC address.

* Thu Jun 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 141-alt6
- rule_generator.functions (choose_rules_file): Print header to empty rules file
  as well as to just created rules file (Dmitry V. Levin)

* Mon Jun 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 141-alt5
- net-agent: ignore hostapd interface mon.*

* Wed Jun 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 141-alt4
- packaged rule-generator

* Thu May 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 141-alt3
- net-agent: ignore pan[0-9]*

* Thu Apr 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 141-alt2
- deleted 94-pam-console.rules

* Thu Apr 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 141-alt1
- New upstream release (141)

* Fri Mar 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 140-alt1
- New upstream release (140)

* Thu Mar 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 139-alt3
- fixed device-mapper support

* Tue Mar 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 139-alt2
- volume_id: ntfs - fixed uuid setting

* Fri Feb 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 139-alt1
- New upstream release (139)

* Tue Feb 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 138-alt3
- init: removed convert_udev_db_from_initramfs calls

* Fri Feb 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 138-alt2
- rules: updated device-mapper/md-raid

* Thu Feb 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 138-alt1
- New upstream release (138)

* Fri Jan 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 137-alt1
- New upstream release (137)

* Tue Jan 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 136-alt2
- added "tape" group
- convert firmware.sh/net.agent to C

* Wed Jan 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 136-alt1
- New upstream release (136)

* Mon Jan 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 135-alt2
- rebuild with klibc-1.5.15

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 135-alt1
- New upstream release (135).

* Thu Nov 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 134-alt1
- New upstream release (134).

* Sat Nov 15 2008 Sergey Vlasov <vsu@altlinux.ru> 130-alt6
- udevadm: fixed option parsing breakage with klibc introduced in
  version 128.  Fixes random reordering of modules included in
  initramfs ("udevadm trigger" options were ignored, causing modules
  for all detected devices to be loaded in undefined order before
  processing the module list built by mkinitrd).

* Sun Oct 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 130-alt5
- fixed /dev/dri/card* permissions

* Thu Oct 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 130-alt4
- libvolume_id-devel/libudev-devel: fixed libdir in pc files

* Wed Oct 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 130-alt3
- fixed unmet on x86_64

* Wed Oct 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 130-alt2
- fixed build for x86_64

* Wed Oct 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 130-alt1
- New upstream release (130).

* Tue Sep 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 127-alt4
- udev-initramfs:
  + drop udev{settle,trigger} link (close #16959)
  + requires mkinitrd-initramfs >= 1:3.0.8-alt1

* Mon Sep 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 127-alt3
- firmware.sh: lookup kernel provided firmware directory

* Mon Sep 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 127-alt2
- fixed %%_libdir for x86_64

* Mon Sep 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 127-alt1
- New upstream release (127).

* Mon Aug 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 126-alt3
- fixed %%_libdir for x86_64

* Mon Aug 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 126-alt2
- fixed change mode bits for CDROM

* Sun Aug 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 126-alt1
- New upstream release (126).

* Sun Aug 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 125-alt3
- updated rules

* Sat Aug 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 125-alt2
- rules cleanup

* Sat Aug 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 125-alt1
- New upstream release (125).

* Tue Jul 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 124-alt3
- drop 80-bluetooth.rules

* Mon Jul 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 124-alt2
- scsi_id: fix fallback to sg v3 for sg nodes
- path_id: suppress trailing '-' like 'ID_PATH=pci-0000:05:01.0-'
- rules: fix cciss rules for partition numbers > 9

* Fri Jun 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 124-alt1
- New upstream release (124).

* Fri Jun 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 122-alt3
- added provides hotplug = 2004_09_23-alt18
- added firmware directory

* Thu Jun 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 122-alt2
- fixed persistent storage rules
- returned /sbin/udevcontrol

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 122-alt1
- New upstream release (122).
- Drop sound.agent

* Tue Apr 01 2008 Sergey Vlasov <vsu@altlinux.ru> 118-alt1
- New upstream release (118).
- Applied post-118 upstream changes (3f91a27d16cf5440f0cb1db7c5972b4924a41d01):
  + update mailing list address in documentation
  + do not skip RUN execution if device node removal fails
  + volume_id: fix UUID raw buffer usage
  + volume_id: add prefix=, exec_prefix=
  + volume_id: fix typo in function documentation
  + volume_id: update ext detection
- Updated udevd initscript:
  + if use_initramfs_dev="1" is set, convert udev database created in initramfs
    to the current format
- udevconvertdb: Add support for 111 -> 112 conversion (udev database format
  has changed again in release 112).
- Updated udev rules:
  + major resync with upstream
  + add usbfs rule for kernels >= 2.6.22
  + disable device file removal for /dev/ppp and /dev/net/tun
  + remove obsolete devfs-style /dev/misc/rtc symlink to /dev/rtc
  + if new-style /dev/rtc0 is present, symlink it to /dev/rtc
  + use ata_id to create persistent links for libata devices (fixes possible
    truncation, but only with kernels >= 2.6.21); old links from SCSI emulation
    info still kept for compatibility
  + do not create by-uuid/by-label links for whole disk devices (such links
    would not be updated properly after media change)
  + use encoded label in persistent links instead of dropping unsafe characters
  + add ENV{REMOVE_CMD} invocation on remove events
  + fix names for bsg and aoe devices
  + ignore modprobe errors when using modalias
  + add rules to autoload tifm_sd, tifm_ms, memstick modules
  + remove broken rules for Tascam USB soundcards (should be moved to
    alsa-firmware after fixing)
  + remove call to nonexistent /etc/alsa.d/udev-soundfont for emu10k1
  + remove broken "/usr/sbin/alsactl -F restore %%n" invocation (#13592)
  + update persistent link creation for device mapper devices:
     + fix symlink priorities for snapshots (previously the symlink would point
       at the original device directly, which would cause snapshot corruption
       if used for writing)
     + add /dev/disk/by-id/dm-name-*, /dev/disk/by-id/dm-uuid-* symlinks

* Wed Nov 28 2007 Sergey Vlasov <vsu@altlinux.ru> 108-alt2
- Applied post-108 upstream changes (0809c264e9878cdd1c61d9fb0e077972bc596ef8):
  + make ACTION!="add|change" working (now "!=" is really the inverse of "==")
  + udevinfo: export all information stored in database
  + udevtest: export ACTION string if given as option
  + udevtest: import uevent variables if possible
- Updated udevd initscript:
  + fixed check for /dev/shm entry in fstab
- Updated udev rules:
  + added /dev/js* compat symlinks for /dev/input/js* (#7669)

* Thu Mar 29 2007 Sergey Vlasov <vsu@altlinux.ru> 108-alt1
- New upstream release (108).
- Note: udev_run_devd and udev_run_hotplugd utilities were removed from udev
  by upstream developers (their usage in rules was removed in 105-alt1).
- Reverted create_floppy_devices change from 0.77-alt3 which was adding the
  "-g <group>" option (in udev-106 the "-G <group>" option was added).
- Updated udevd initscript:
  + added "start_udev_only" action for use during package upgrade;
  + removed setting kernel.hotplug to /sbin/hotplug on stop.
- Updated udev rules:
  + updated create_floppy_devices options for new implementation in udev-106;
  + removed useless dasd support (s390 only);
  + added persistent symlinks for SCSI tapes and medium changer devices;
  + fixed WAIT_FOR_SYSFS for SCSI devices;
  + fixed wrong rule for raw devices (/dev/raw/raw[0-9]*);
  + added -b option to all modprobe invocations;
  + disabled MODALIAS autoload for the i82365 module (Debian bug #398962);
  + added SUBSYSTEM and ACTION checks to rules for ALSA devices;
  + added checks to avoid normal rules for net devices (Gentoo bug #166652);
  + added rules to create /dev/disk/{by-uuid,by-label}/* links for md devices
    (63-md.rules); these rules are also copied to initramfs (#11190).
- Added /usr/sbin/udevconvertdb utility to convert udev database to the new
  format used since udev-107; updated %%pre and %%post scripts to convert the
  database during upgrade.

* Mon Feb 19 2007 Sergey Vlasov <vsu@altlinux.ru> 105-alt3
- Added conflicts with old udev packages to the udev-rules subpackage
  (prevents attempts to install udev-rules together with old releases of
  udev which had rule files in the main package).
- Updated udevd initscript:
  + removed broken code which tried to remove old udev database on start;
  + fixed compatibility with startup-0.9.8.9-alt1:
     + pass -n option to mount when running from rc.sysinit;
     + do not try to start another copy of udevd if already running;
     + use $tmpfs_options when mounting /dev initially;
     + do not try to remount /dev when running from rc.sysinit;
     + do not unmount /dev on stop (this time "service udevd umount" added
       for use during dev package upgrade).
     + fix double /dev/shm mounting if it is listed in fstab
- Updated net.agent:
  + check for ignored interface name first (fixes useless failure during
    early startup of interfaces like "lo").

* Sun Feb 11 2007 Sergey Vlasov <vsu@altlinux.ru> 105-alt2
- Fixed net.agent to avoid unwanted dependency on etcnet; now net-scripts
  should be usable again.
- Moved module-init-tools, dmsetup, libvolume_id from Requires to PreReq
  (these packages should be installed before udev to keep rules working).
- Moved rule files to a separate udev-rules package; replaced dependency of
  udev-initramfs on udev with udev-rules (now installing new mkinitrd with
  initramfs support does not require the main udev package).
- Added Provides: /etc/udev/rules.d, /etc/udev/initramfs-rules.d to the
  udev-rules subpackage to be used by other packages with udev rules.
- Updated udevd initscript:
  + do not invoke udevtrigger during restart (avoids bad side effects with
    some devices, but events which happen during restart will be lost)
  + unmount /dev on stop again (reverts the change made in 105-alt1;
    workaround for upgrading the dev package); unmount is not performed on
    restart and condrestart
- Updated udev rules:
  + removed rule for loading the pcmcia module (already in pcmciautils)

* Thu Feb 08 2007 Sergey Vlasov <vsu@altlinux.ru> 105-alt1
- New upstream release (105).
- Dropped git-scsi_id-garbage patch (fixed upstream).
- Replaced old package build system with a new one based on the upstream git
  repository, rewritten spec file for the new layout:
    + applied all old patches as commits in the package git repository
    + placed udev rules in etc/udev/altlinux/
    + placed udevd initscript in etc/init.d/
    + placed dm_helper in extras/dm_helper/
- Added udev-initramfs subpackage which contains udev built with klibc for
  use in initramfs images created by mkinitrd.
- Added /etc/udev/initramfs-rules.d directory containing symlinks to rule
  files which need to be copied to initramfs.
- Disabled recursive substititions in udev_rules_apply_format() (this feature
  is dubious, dangerous if used improperly (e.g., there is no protection from
  infinite loops) and does not seem to be documented properly).
- libvolume_id: Fixed possible buffer overruns when handling romfs and
  ntfs filesystems, and other filesystems with too long labels.
- Updated udev rules:
  + moved rules for ignoring of "drivers" and "module" events from
    20-hotplugd.rules to 05-udev-early.rules
  + fixed rule for removable IDE avoidance to use ATTR{removable} instead of
    ATTRS{removable}
  + added rules to create /dev/disk/{by-uuid,by-label}/* links for devices
    managed by the device mapper driver (64-device-mapper.rules)
  + added rule to invoke /sbin/pam_console_apply in 94-pam-console.rules
    (fixes wrong permissions for devices managed by pam_console if these
    devices appeared after login, or if udevtrigger was rerun)
  + removed callouts to the hotplug package - now modprobe by modalias is
    used to load kernel modules, and other actions are handled by scripts
    included in the udev package (currently net.agent and sound.agent).
- Updated udevd initscript:
  + do not unmount /dev on stop (breaks too much to be useful)
  + implement condrestart instead of ignoring it (now udevd will be
    restarted during package upgrade, like all other daemons)
- Added udevd-final service to perform final steps of udev initialization
  when other parts of the system have been initialized.

* Sun Dec 17 2006 Sergey Vlasov <vsu@altlinux.ru> 103-alt1
- Added patches:
  + git-scsi_id-garbage: scsi_id: remove trailing garbage from ID_SERIAL_SHORT
- Updated udev rules:
  + restore lost rules for firmware loading
  + kill useless NAME="%%k" assignments
  + resync 50-udev-default.rules with SUSE:
     + create /dev/pilot symlink also for Handspring Treo devices
     + create all possible partitions for ide-floppy devices
     + load mmc_block module for MMC devices
     + fix device names for (obsolete) raw devices (/dev/raw/rawN)
     + check for ACTION=="add" when creating /dev/bus/usb/** devices
  + fix permissions for floppy devices (GROUP="floppy", MODE="0660")
  + resync 60-persistent-storage.rules with SUSE:
     + add /dev/disk/by-id/ata-* symlinks for libata and other SAT devices
     + add /dev/disk/by-id/mmc-* symlinks for MMC block devices
  + replace DRIVER key with DRIVERS

* Thu Oct 26 2006 Anton Farygin <rider@altlinux.ru> 103-alt0.1
- Updated patches to new version
- removed patches:
    udev-097-alt-nogroup.patch (included to mainstream)

* Fri Sep 01 2006 Sergey Vlasov <vsu@altlinux.ru> 097-alt2
- Added patches:
  + alt-init-pipe-before-fork: udevd: init signal pipe before forking to
    background
  + alt-udevd-pidfile: udevd: add pid file support (/dev/.udev/udevd.pid)
- Updated udevd initscript:
  + use pid file in /dev/.udev/udevd.pid
  + daemonize with "udevd --daemon" instead of "start_daemon --make-pidfile"
    (should really fix startup race with udevsettle - #9881)
  + revert broken fix for #9881 added in 097-alt1

* Mon Aug 28 2006 Sergey Vlasov <vsu@altlinux.ru> 097-alt1
- New version (097).
- Dropped alt-compile-warnings patch (obsolete).
- Removed obsolete "--with klibc" build support from spec (upstream developers
  removed klibc support from udev 097).
- Removed obsolete "--with system_sysfs" build support from spec (udev does not
  use libsysfs for a long time).
- Tightened udev package dependency on libvolume_id due to unstable ABI.
- Removed tmpfs_options example with "helper" from udev.conf (the corresponding
  kernel patch was dropped long ago).
- Added alt-nogroup patch: vol_id: replace "nogroup" group name with "nobody"
  (partially fixes #9871).
- Replaced logger-path patch with alt-firmware-initlog patch: use /sbin/initlog
  instead of logger (which is in /usr/bin).
- Added alt-firmware-dirs patch: add /usr/lib/hotplug/firmware to firmware
  search path (to avoid regressions when firmware loading is switched from
  hotplug to udev).
- Updated udevd initscript:
  + fixed udevsettle race (#9881); removed broken workaround added in 091-alt3
  + add "-n" option to "mount --move" to fix duplication of /etc/mtab entries
    (#7758)
  + check that all required kernel features (/sys/class/mem/null/uevent,
    /sys/kernel/uevent_seqnum) are present before trying to start udevd
  + removed code for handling udevd started from hotplug (udev does not support
    this for a long time)
  + removed useless $mountcmd indirection from attach_pts_filesystem and
    attach_shm_filesystem
  + fixed /dev/null redirections in make_extra_nodes, removed /dev/null usage
    from places where /dev/null is not yet available
- Updated udev rules:
  + moved all WAIT_FOR_SYSFS rules to 05-udev-early.rules
  + moved firmware loading rules to 05-udev-early.rules, so that they are used
    before hotplug (previously both hotplug and udev were trying to load
    firmware; now all firmware loading is handled through udev)
  + removed useless rule which "renamed" eth* network interfaces to the same
    name
  + added joystick support to 60-persistent-input.rules
  + added crypto container support to 60-persistent-storage.rules
  + removed fuse rule (#9871)
  + removed /dev/tpm* rule with "tss" user/group (#9871)
  + removed /dev/ucm*, /dev/uverbs* rules with "rdma" group (#9871)
  + removed rules for SCSI scanners with "scanner" group (#9871)
  + removed /dev/nvram rule with "nvram" group (#9871)
  + replaced "tape" group with "disk", removed some rules which were setting
    the "tape" group for devices which already had the "disk" group from other
    rules (#9871)
  + removed "video" group from agpgart, DRI and framebuffer devices (now this
    group is used only for video capture devices)
- Create "video" group in %%pre (#9871).

* Mon Jul 10 2006 Anton Farygin <rider@altlinux.ru> 096-alt1
- new version

* Tue Jun 20 2006 Anton Farygin <rider@altlinux.ru> 094-alt1
- new version

* Thu Jun 01 2006 Anton Farygin <rider@altlinux.ru> 093-alt3
- fixed SUBSYSTEM and SYSFS errors in rules

* Tue May 30 2006 Anton Farygin <rider@altlinux.ru> 093-alt2
- fixed logger unmet

* Mon May 29 2006 Anton Farygin <rider@altlinux.ru> 093-alt1
- new version
- updated rules for new firmware loader

* Thu May 18 2006 Anton Farygin <rider@altlinux.ru> 092-alt1
- new version
- added lvm support (#7369, Nick S. Grechukh)

* Tue May 16 2006 Anton Farygin <rider@altlinux.ru> 091-alt3
- added workaround (sync) for tmpfs files creation race in initscript

* Sat May 06 2006 Anton Farygin <rider@altlinux.ru> 091-alt2
- package adopted to gear
- added patch from mainstream for creating parent directories for seqnum

* Fri Apr 28 2006 Anton Farygin <rider@altlinux.ru> 091-alt1
- new version

* Fri Apr 21 2006 Anton Farygin <rider@altlinux.ru> 090-alt2
- added sleep after udevtrigger

* Sun Apr 16 2006 Anton Farygin <rider@altlinux.ru> 090-alt1
- new version

* Fri Apr 14 2006 Anton Farygin <rider@altlinux.ru> 089.git20060414-alt0.3
- updated from git
- added udevsettle to initscript

* Wed Apr 12 2006 Anton Farygin <rider@altlinux.ru> 089-alt0.2
- path_id added

* Tue Apr 11 2006 Anton Farygin <rider@altlinux.ru> 089-alt0.1
- new version
- all rules changed for new udev policy

* Mon Mar 13 2006 Anton Farygin <rider@altlinux.ru> 0.77-alt3
- added rule for floppy devices creation (#9129)
- Zaptel devices removed from rules (#8753)
- Firmware loading fixed (thnx , lioka)
- fixed typo in initscript

* Tue Feb 21 2006 Anton Farygin <rider@altlinux.ru> 0.77-alt2
- fixed /dev/pts start and restart

* Wed Dec 14 2005 Anton Farygin <rider@altlinux.ru> 0.77-alt1
- new version
- use new regexp for initscript (#8061)
- fixed /dev premissions

* Tue Nov 15 2005 Anton Farygin <rider@altlinux.ru> 0.75-alt1
- next version

* Mon Sep 19 2005 Anton Farygin <rider@altlinux.ru> 0.70-alt1
- new version
- added rule for ttyACM
- fixed rule for /dev/tty (#8026)

* Wed Aug 31 2005 Anton Farygin <rider@altlinux.ru> 0.68-alt2
- fixed double /dev/pts mounting (#6974)

* Fri Aug 19 2005 Anton Farygin <rider@altlinux.ru> 0.68-alt1
- new version

* Mon Aug 08 2005 Anton Farygin <rider@altlinux.ru> 0.65-alt1
- updated to new version
- fixed typo in rules (#7394)

* Sun Jul 17 2005 Anton Farygin <rider@altlinux.ru> 0.63-alt2
- removed patch1 (included to mainstream)
- removed patch0 (use OPTIONS="ignore_device" for ACTION=="remove")
- requries to udev_static_addon added
- fixed rules for vizor (#7394)

* Wed Jul 13 2005 Anton Farygin <rider@altlinux.ru> 0.62-alt5
- fixed some bugs in rules

* Wed Jul 13 2005 Anton Farygin <rider@altlinux.ru> 0.62-alt4
- rules format updated

* Wed Jul 13 2005 Anton Farygin <rider@altlinux.ru> 0.62-alt3
- added rule for running scripts from hotplug.d and dev.d
- udev initscript remove hotplug execution from /proc/sys/kernel/hotplug

* Tue Jul 12 2005 Anton Farygin <rider@altlinux.ru> 0.62-alt2
- updated to 062

* Wed Mar 30 2005 Alexey Morozov <morozov@altlinux.org> 0.50-alt5
- Fixes for init script for empty and r/o /dev

* Tue Mar 29 2005 Alexey Morozov <morozov@altlinux.org> 0.50-alt4
- init script fixes
- udev lsb rules fixes (#6232, #6297, #6338, and probably #6337)
- built w/ syslog (#5850)
- possible integration w/ udev_static-*

* Sat Jan 22 2005 Alexey Morozov <morozov@altlinux.org> 0.50-alt3
- fixed typo in udevd.init (now service should start w/o complaining
  even if no devices in /etc/udev/devices can be found)
- udevd is forced to stop, even if it was launched not by init startup
  script
- added patch to skip unknown (new) options from udev.conf throughout
  C code (udevinfo, udev etc). Bug was reported by vk@.

* Fri Jan 14 2005 Alexey Morozov <morozov@altlinux.org> 0.50-alt2
- Use syslog by default (#5850)
- Added udevinfo prints patch from ML
- Preliminary support of modules_lookup
- Actual use of tmpfs_options
- Added directory %_sysconfdir/udev/devices as a workaround for
  "missing devices" problem. One can create required device inodes
  with /sbin/MAKEDEV -d /etc/udev/devices <devname>, and all these
  inodes will be copied as is to /dev upon udev startup.
- DO_TRADITIONAL and PREFER_TRADITIONAL removed from cd-names.sh
  Traditional names if needed now should be specified right in udev rules

* Tue Jan  4 2005 Alexey Morozov <morozov@altlinux.org> 0.50-alt1
- New version (0.50)

* Tue Dec 28 2004 Alexey Morozov <morozov@altlinux.org> 0.46-alt3
- extended modifiers are fixed [hopefully]
- ide-names.sh replaced by drive-names.sh which can be used for SCSI disks (only sd*)
  as well as as for IDE drives (either IDE hard disks, CD-ROMs, or IDE floppies)

* Tue Dec 14 2004 Alexey Morozov <morozov@altlinux.org> 0.46-alt2
- Fixed CD-ROMs / CD-RWs etc permissions

* Tue Dec 14 2004 Alexey Morozov <morozov@altlinux.org> 0.46-alt1
- version 0.46 (046)
- service init script greatly improved. Now it passes multiple start/stop etc cycles almost seamlessly
- permissions and device naming rules also improved (mostly taked from Mdk w/ certain Debian stuff
  and home-made ide-names.sh and cd-names.sh). Device naming rules are still subject for improvement and
  bugfixing though...
- Added patches for %%N and %%U rules keys (see 'man 8 udev' for description)
- Fixes for %%e
- TODO: write a SCSI-oriented companion for ide-names.sh. Contrubutors are welcome ;-)

* Thu Nov 11 2004 Alexey Morozov <morozov@altlinux.org> 0.43-alt1
- New version (0.43)
- Spec and patches are re-worked a bit (now it can be correctly build w/ and w/o
  system sysfs)

* Thu Sep 16 2004 Alexey Morozov <morozov@altlinux.org> 0.32-alt1
- Initial build for ALT Linux

