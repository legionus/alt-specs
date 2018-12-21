%define mname kvm
Name: kernel-src-%mname
Version: 3.10.21
Release: alt8
Summary: KVM modules sources for Linux kernel
Group: Development/Kernel
BuildArch: noarch
License: GPLv2+
URL: http://www.linux-kvm.org
Source: %mname-kmod-%version.tar
Patch: %mname-kmod-%version-alt.patch
Provides: kernel-source-%mname = %version-%release

BuildRequires: rpm-build-kernel

%description
This package contains KVM modules sources for Linux kernel.


%prep
%setup -q -n %mname-kmod-%version
%patch -p1


%install
install -d -m 0755 %buildroot%kernel_src
D="$(basename "$PWD")"
tar -C .. --transform "s/^$D/%mname-%version/" -cJf %buildroot%kernel_src/%mname-%version.tar.xz "$D"


%files
%_usrsrc/kernel


%changelog
* Tue May 13 2014 Led <led@altlinux.ru> 3.10.21-alt8
- updates from linux-3.10.40:
  + KVM: ioapic: fix assignment of ioapic->rtc_status.pending_eoi (CVE-2014-0155)

* Wed Apr 02 2014 Led <led@altlinux.ru> 3.10.21-alt7
- updates from linux-3.10.35:
  + KVM: MMU: handle invalid root_hpa at __direct_map
  + KVM: x86: handle invalid root_hpa everywhere
  + KVM: VMX: fix use after free of vmx->loaded_vmcs

* Fri Mar 21 2014 Led <led@altlinux.ru> 3.10.21-alt6
- updates from linux-3.10.34:
  + KVM: SVM: fix cr8 intercept window

* Tue Mar 04 2014 Led <led@altlinux.ru> 3.10.21-alt5
- updates from linux-3.10.33:
  + kvm: x86: fix emulator buffer overflow (CVE-2014-0049)

* Fri Feb 21 2014 Led <led@altlinux.ru> 3.10.21-alt4
- updates from linux-3.10.32:
  + KVM: return an error code in kvm_vm_ioctl_register_coalesced_mmio()

* Sun Feb 02 2014 Led <led@altlinux.ru> 3.10.21-alt3
- updates from linux-3.10.29:
  + kvm: x86: fix apic_base enable check

* Sun Jan 12 2014 Led <led@altlinux.ru> 3.10.21-alt2
- updates from linux-3.10.26:
  + KVM: x86: Fix APIC map calculation after re-enabling

* Thu Dec 19 2013 Led <led@altlinux.ru> 3.10.21-alt1
- 3.10.21
- updates from linux-3.10.25:
  + CVE-2013-4587
  + CVE-2013-6367
  + CVE-2013-6368
  + CVE-2013-6376

* Mon Dec 02 2013 Led <led@altlinux.ru> 3.10.1-alt3
- x86: fix emulation of "movzbl %%bpl, %%eax"
- IOMMU: hva align mapping page size

* Wed Nov 06 2013 Led <led@altlinux.ru> 3.10.1-alt2
- use a more sensible error number when debugfs directory creation fails

* Mon Aug 05 2013 Led <led@altlinux.ru> 3.10.1-alt1
- 3.10.1

* Sat Jul 27 2013 Led <led@altlinux.ru> 3.9.10-alt1
- 3.9.10

* Sat Jul 06 2013 Led <led@altlinux.ru> 3.9.8-alt2
- updated summary and description

* Sun Jun 30 2013 Led <led@altlinux.ru> 3.9.8-alt1
- 3.9.8

* Sat Jun 22 2013 Led <led@altlinux.ru> 3.9-alt1
- 3.9

* Sat Jun 22 2013 Led <led@altlinux.ru> 3.8-alt1
- 3.8

* Thu Jun 20 2013 Led <led@altlinux.ru> 3.7.6-alt1
- 3.7.6

* Mon Nov 05 2012 Led <led@altlinux.ru> 3.6-alt1
- 3.6

* Thu Oct 25 2012 Led <led@altlinux.ru> 3.5.4-alt1
- 3.5.4

* Thu Aug 02 2012 Led <led@massivesolutions.co.uk> 3.5-cx0
- 3.5

* Thu May 24 2012 Led <led@massivesolutions.co.uk> 3.4-cx0
- 3.4

* Sat May 12 2012 Led <led@massivesolutions.co.uk> 3.3-cx0
- 3.3

* Fri Jan 20 2012 Led <led@massivesolutions.co.uk> 3.2-cx0
- 3.2

* Sun Nov 20 2011 Led <led@massivesolutions.co.uk> 3.1-cx0
- 3.1

* Fri Aug 19 2011 Led <led@massivesolutions.co.uk> 3.0b-cx0
- initial build
