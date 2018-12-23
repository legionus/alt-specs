%def_without check
%def_without ksrc
%def_without xenserver
%def_with debugtools
%def_with dpdk
%def_with python3

Name: openvswitch
Version: 2.10.1
Release: alt1

Summary: An open source, production quality, multilayer virtual switch
License: Apache-2.0 and LGPLv2+ and SISSL
Group: Networking/Other

Url: http://openvswitch.org
Source0: %url/releases/%name-%version.tar
Source1: %name.init
Source3: 01-%name
Source4: create-ovsbr
Source5: create-ovsbond
Source6: create-ovsport
Source7: destroy-ovsbr
Source8: destroy-ovsbond
Source9: destroy-ovsport
Source10: setup-ovsbr
Source12: %name.tmpfiles

Patch1: openvswitch-2.0_alt_fix_function.patch
Patch2: openvswitch-2.5.0-fix-link.patch
Patch3: openvswitch-2.9.2-alt-systemd-unit.patch
Patch4: openvswitch-2.10-netdev-dpdkv18.08.patch

Obsoletes: %name-controller <= %name-%version
Obsoletes: %name-ovsdbmonitor <= %name-%version

# util-linux-2.32-alt2
Requires: pam0(runuser)

BuildRequires: graphviz libssl-devel openssl groff
BuildRequires: libcap-ng-devel
BuildRequires: glibc-kernheaders
BuildRequires: python-modules python-modules-logging python-modules-xml python-module-flake8 python-module-six python-module-sphinx python-devel python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-six
%endif

%{?_with_dpdk:BuildRequires: dpdk-devel >= 18.08 libpcap-devel libnuma-devel}

%define ksrcdir %_usrsrc/kernel/sources

%description
Open vSwitch is a production quality, multilayer virtual switch
licensed under the open source Apache 2.0 license. It is designed
to enable massive network automation through programmatic
extension, while still supporting standard management interfaces
and protocols (e.g. NetFlow, sFlow, RSPAN, ERSPAN, CLI, LACP,
802.1ag). In addition, it is designed to support distribution
across multiple physical servers similar to VMware's vNetwork
distributed vswitch or Cisco's Nexus 1000V.

%if_with ksrc
%package -n kernel-source-%name
Group: Development/Kernel
License: GPLv2+
Summary: Open vSwitch Linux kernel modules source
BuildArch: noarch

%description -n kernel-source-%name
Source for kernel modules supporting the openvswitch datapath
%endif

%if_with debugtools
%package debugtools
Group: Networking/Other
License: Apache-2.0
Summary: Open vSwitch bug reporting tool
BuildArch: noarch
Requires: %name-common = %EVR

%description debugtools
This package contains ovs-bugtool to generate a debug bundle
with useful information about Open vSwitch on this system
and place it in %_logdir/ovs-bugtool, and ovs-test to check
Linux drivers for performance and vlan problems.
%endif

%package common
Group: Networking/Other
License: Apache-2.0 and LGPLv2+ and SISSL
Summary: Common Open vSwitch code

%description common
This package provides components required by both openvswitch
and openvswitch-controller.

%package vtep
Group: Networking/Other
License: Apache-2.0
Summary: Open vSwitch VTEP emulator
Requires: %name = %EVR

%description vtep
A VTEP emulator that uses Open vSwitch for forwarding.

%package devel
Summary: Open vSwitch Devel Libraries
License: Apache-2.0
Group: Development/C
Requires: %name = %EVR

%description devel
Devel files for Open vSwitch.

%package ovn-central
Summary: Open vSwitch - Open Virtual Network support
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR
Requires: %name-ovn-common = %EVR

%description ovn-central
OVN, the Open Virtual Network, is a system to support virtual network
abstraction.  OVN complements the existing capabilities of OVS to add
native support for virtual network abstractions, such as virtual L2 and L3
overlays and security groups.

%package ovn-host
Summary: Open vSwitch - Open Virtual Network support
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR
Requires: %name-ovn-common = %EVR

%description ovn-host
OVN, the Open Virtual Network, is a system to support virtual network
abstraction.  OVN complements the existing capabilities of OVS to add
native support for virtual network abstractions, such as virtual L2 and L3
overlays and security groups.

%package ovn-vtep
Summary: Open vSwitch - Open Virtual Network support
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR
Requires: %name-ovn-common = %EVR

%description ovn-vtep
OVN vtep controller

%package ovn-common
Summary: Open vSwitch - Open Virtual Network support
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR

%description ovn-common
Utilities that are use to diagnose and manage the OVN components.

%package ovn-docker
Summary: Open vSwitch - Open Virtual Network support
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR
Requires: %name-ovn-common = %EVR
Requires: python-module-%name = %EVR
 
%description ovn-docker
Docker network plugins for OVN.

%package -n python-module-%name
Summary: Open vSwitch python bindings
Group: Development/Python
License: Python-2.0
BuildArch: noarch
%add_python_req_skip pywintypes win32con win32file msvcrt

%description -n python-module-%name
Python bindings for the Open vSwitch database

%package -n python3-module-%name
Summary: Open vSwitch python3 bindings
Group: Development/Python3
License: Python-2.0
BuildArch: noarch
%add_python3_req_skip pywintypes win32con win32file msvcrt

%description -n python3-module-%name
Python3 bindings for the Open vSwitch database

%package -n bash-completion-%name
Summary: Bash completion for systemd utils
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: %name = %EVR

%description -n bash-completion-%name
Bash completion for %name.

%prep
%setup
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

%if_with ksrc
# it's not datapath/linux due to shared configure script; thx led@
pushd ..
mkdir kernel-source-%name-%version
cp -al  %name-%version/{config.h.in,configure,Makefile.in} \
	%name-%version/{build-aux,datapath,include,tests} \
	kernel-source-%name-%version/
tar cf kernel-source-%name-%version.tar kernel-source-%name-%version
rm -r kernel-source-%name-%version
popd
%endif

%build
%autoreconf
%configure \
	--disable-static \
	--enable-shared \
	--enable-ssl \
%if_with dpdk
	--with-dpdk=$(dirname %_libdir/dpdk/*/.config) \
%endif
	--with-rundir=%_runtimedir/%name \
	--with-logdir=%_logdir/%name \
	--with-dbdir=%_localstatedir/%name \
	--with-pkidir=%_localstatedir/%name/pki

%make_build
make rhel/usr_lib_systemd_system_ovs-vswitchd.service

# test 591 fails, reported upstream
%if_with check
%check
LC_CTYPE=en_US.UTF-8 LC_COLLATE=en_US.UTF-8 make check
%endif

%install
%makeinstall_std

%if_with ksrc
mkdir -p %buildroot%ksrcdir
install -pm0644 ../kernel-source-%name-%version.tar %buildroot%ksrcdir/
%endif

install -dm0755 %buildroot%_sysconfdir/%name
install -pDm0755 %SOURCE1 %buildroot%_initdir/%name
install -dm0755 %buildroot%_runtimedir/%name
install -dm0750 %buildroot%_logdir/%name
install -dm0755 %buildroot%_sysconfdir/%name

install -pDm0644 vswitchd/vswitch.ovsschema \
         %buildroot%_datadir/%name/vswitch.ovsschema
install -pDm0644 rhel/etc_logrotate.d_openvswitch \
         %buildroot%_sysconfdir/logrotate.d/%name
install -pDm0644 rhel/usr_share_openvswitch_scripts_sysconfig.template \
         %buildroot/%_sysconfdir/sysconfig/%name
install -pDm0644 rhel/etc_openvswitch_default.conf \
	 %buildroot/%_sysconfdir/openvswitch/default.conf

for service in openvswitch ovsdb-server ovs-vswitchd ovs-delete-transient-ports \
                ovn-controller ovn-controller-vtep ovn-northd; do
    install -pDm0644 \
            rhel/usr_lib_systemd_system_${service}.service \
            %buildroot%_unitdir/${service}.service
done

#etcnet
install -pDm644 %SOURCE3 %buildroot%_sysconfdir/net/options.d/01-openvswitch
install -pDm755 %SOURCE4 %buildroot%_sysconfdir/net/scripts/create-ovsbr
install -pDm755 %SOURCE5 %buildroot%_sysconfdir/net/scripts/create-ovsbond
install -pDm755 %SOURCE6 %buildroot%_sysconfdir/net/scripts/create-ovsport
install -pDm755 %SOURCE7 %buildroot%_sysconfdir/net/scripts/destroy-ovsbr
install -pDm755 %SOURCE8 %buildroot%_sysconfdir/net/scripts/destroy-ovsbond
install -pDm755 %SOURCE9 %buildroot%_sysconfdir/net/scripts/destroy-ovsport
install -pDm755 %SOURCE10 %buildroot%_sysconfdir/net/scripts/setup-ovsbr

install -pDm644 %SOURCE12 %buildroot%_tmpfilesdir/%name.conf

# FIXME
%if_with xenserver
install -pDm755 xenserver/etc_init.d_openvswitch-xapi-update \
         %buildroot%_initdir/openvswitch-xapi-update
install -pDm755 xenserver/etc_xapi.d_plugins_openvswitch-cfg-update \
         %buildroot%_sysconfdir/xapi.d/plugins/openvswitch-cfg-update
install -pDm755 xenserver/opt_xensource_libexec_interface-reconfigure \
             %buildroot%_datadir/%name/scripts/interface-reconfigure
install -pDm644 xenserver/opt_xensource_libexec_InterfaceReconfigure.py \
             %buildroot%_datadir/%name/scripts/InterfaceReconfigure.py
install -pDm644 xenserver/opt_xensource_libexec_InterfaceReconfigureBridge.py \
             %buildroot%_datadir/%name/scripts/InterfaceReconfigureBridge.py
install -pDm644 xenserver/opt_xensource_libexec_InterfaceReconfigureVswitch.py \
             %buildroot%_datadir/%name/scripts/InterfaceReconfigureVswitch.py
install -pDm755 xenserver/etc_xensource_scripts_vif \
             %buildroot%_datadir/%name/scripts/vif
install -pDm644 xenserver/usr_share_openvswitch_scripts_sysconfig.template \
         %buildroot%_datadir/%name/scripts/sysconfig.template
install -pDm644 \
        xenserver/usr_lib_xsconsole_plugins-base_XSFeatureVSwitch.py \
               %buildroot%_libdir/xsconsole/plugins-base/XSFeatureVSwitch.py
%endif

install -d -m 0755 %buildroot%python_sitelibdir_noarch
cp -a %buildroot%_datadir/%name/python/* %buildroot%python_sitelibdir_noarch
install -d -m 0755 %buildroot%python3_sitelibdir_noarch
cp -a %buildroot%_datadir/%name/python/ovs %buildroot%python3_sitelibdir_noarch
rm -rf %buildroot%_datadir/%name/python

touch %buildroot%_sysconfdir/%name/conf.db
touch %buildroot%_sysconfdir/%name/system-id.conf
mkdir -p %buildroot%_logdir/%name

# remove unpackaged files
rm -f %buildroot%_bindir/ovs-benchmark \
    %buildroot%_bindir/ovs-parse-backtrace \
    %buildroot%_sbindir/ovs-vlan-bug-workaround \
    %buildroot%_man1dir/ovs-benchmark.1* \
    %buildroot%_man8dir/ovs-parse-backtrace.8* \
    %buildroot%_man8dir/ovs-vlan-bug-workaround.8* \
    %buildroot%_datadir/openvswitch/scripts/ovs-save
%pre common
%_sbindir/groupadd -r -f %name
%_sbindir/useradd -r -n -g %name -d / -s /sbin/nologin -c 'openvswitch server daemon' %name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS.rst LICENSE NEWS NOTICE README.rst
%_bindir/ovs-dpctl
%_bindir/ovs-dpctl-top
%_bindir/ovs-testcontroller
%_bindir/ovs-docker
%_bindir/ovs-vsctl
%_bindir/ovsdb-tool
%_sbindir/ovs-vswitchd
%_sbindir/ovsdb-server
%_initdir/%name
%_unitdir/%name.service
%_unitdir/ovs-vswitchd.service
%_unitdir/ovsdb-server.service
%_unitdir/ovs-delete-transient-ports.service
%_tmpfilesdir/%name.conf
%_man1dir/ovsdb-server.1*
%_man1dir/ovsdb-tool.1*
%_man5dir/ovs-vswitchd.conf.db.5*
%_man5dir/ovsdb-server.5*
%_man5dir/ovsdb.5*
%_man7dir/ovs-fields.7*
%_man7dir/ovsdb-server.7*
%_man7dir/ovsdb.7*
%_man8dir/ovs-ctl.8*
%_man8dir/ovs-dpctl.8*
%_man8dir/ovs-dpctl-top.8*
%_man8dir/ovs-kmod-ctl.8*
%_man8dir/ovs-testcontroller.8*
%_man8dir/ovs-vsctl.8*
%_man8dir/ovs-vswitchd.8*

%_datadir/%name/vswitch.ovsschema
%_datadir/%name/scripts/ovs-lib
%_datadir/%name/scripts/ovs-ctl
%_datadir/%name/scripts/ovs-check-dead-ifs
%_datadir/%name/scripts/ovs-kmod-ctl
%dir %_sysconfdir/openvswitch
%config(noreplace) %ghost %_sysconfdir/openvswitch/conf.db
%config(noreplace) %ghost %_sysconfdir/openvswitch/system-id.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/openvswitch/default.conf
%config(noreplace) %_sysconfdir/logrotate.d/openvswitch
%config(noreplace) %_sysconfdir/net/options.d/01-openvswitch
%_sysconfdir/net/scripts/*

%if_with debugtools
%files debugtools
%_bindir/ovs-test
%_bindir/ovs-vlan-test
%_bindir/ovs-l3ping
%_bindir/ovs-pcap
%_bindir/ovs-tcpdump
%_bindir/ovs-tcpundump
%_sbindir/ovs-bugtool
%_man8dir/ovs-bugtool.8*
%_man8dir/ovs-l3ping.8*
%_man8dir/ovs-test.8*
%_man8dir/ovs-vlan-test.8*
%_man1dir/ovs-pcap.1*
%_man8dir/ovs-tcpdump.8*
%_man1dir/ovs-tcpundump.1*
%_datadir/%name/bugtool-plugins/
%_datadir/%name/scripts/ovs-bugtool*
%python_sitelibdir_noarch/ovstest
%endif

%files common
%_logdir/%name
%_localstatedir/%name
%_runtimedir/%name
%_libdir/*.so.*
%_bindir/ovs-appctl
%_bindir/ovn-detrace
%_bindir/ovs-ofctl
%_bindir/ovs-pki
%_bindir/ovsdb-client
%_man1dir/ovsdb-client.1*
%_man1dir/ovn-detrace.1*
%_man8dir/ovs-appctl.8*
%_man8dir/ovs-ofctl.8*
%_man8dir/ovs-pki.8*

# TODO
#files ipsec
#_initdir/openvswitch-ipsec

%files vtep
%_bindir/vtep-ctl
%_man5dir/vtep.5.*
%_man8dir/vtep-ctl.8.*
%_datadir/%name/scripts/ovs-vtep
%_datadir/%name/vtep.ovsschema

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc


%files ovn-docker
%_bindir/ovn-docker-overlay-driver
%_bindir/ovn-docker-underlay-driver

%files ovn-common
%_bindir/ovn-nbctl
%_bindir/ovn-sbctl
%_bindir/ovn-trace
%_datadir/openvswitch/scripts/ovn-ctl
%_datadir/openvswitch/scripts/ovndb-servers.ocf
%_datadir/openvswitch/scripts/ovn-bugtool-nbctl-show
%_datadir/openvswitch/scripts/ovn-bugtool-sbctl-lflow-list
%_datadir/openvswitch/scripts/ovn-bugtool-sbctl-show
%_man8dir/ovn-ctl.8*
%_man8dir/ovn-nbctl.8*
%_man8dir/ovn-trace.8*
%_man7dir/ovn-architecture.7*
%_man8dir/ovn-sbctl.8*
%_man5dir/ovn-nb.5*
%_man5dir/ovn-sb.5*

%files ovn-central
%_bindir/ovn-northd
%_mandir/man8/ovn-northd.8*
%_datadir/openvswitch/ovn-nb.ovsschema
%_datadir/openvswitch/ovn-sb.ovsschema
%_unitdir/ovn-northd.service

%files ovn-host
%_bindir/ovn-controller
%_man8dir/ovn-controller.8*
%_unitdir/ovn-controller.service

%files ovn-vtep
%_bindir/ovn-controller-vtep
%_man8dir/ovn-controller-vtep.8*
%_unitdir/ovn-controller-vtep.service

%files -n python-module-openvswitch
%python_sitelibdir_noarch/ovs

%if_with python3
%files -n python3-module-openvswitch
%python3_sitelibdir_noarch/ovs
%endif

%files -n bash-completion-%name
%_sysconfdir/bash_completion.d/*

%if_with ksrc
%files -n kernel-source-%name
%ksrcdir/*
%endif

%changelog
* Tue Oct 30 2018 Alexey Shabalin <shaba@altlinux.org> 2.10.1-alt1
- 2.10.1

* Thu Sep 13 2018 Anton Farygin <rider@altlinux.ru> 2.10.0-alt1%ubt
- 2.10.0

* Fri Jun 01 2018 Anton Farygin <rider@altlinux.ru> 2.9.2-alt1%ubt
- 2.9.2
- removed selinux policy subpackage

* Thu Aug 03 2017 Anton Farygin <rider@altlinux.ru> 2.7.2-alt1%ubt
- 2.7.2

* Thu Jul 13 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1
- 2.7.1 with security fixes:
  + CVE-2017-9214 Buffer overrread in ofputil_pull_queue_get_config_reply10().
  + CVE-2017-9263 remote DoS attack by a malicious switch.
  + CVE-2017-9265 buffer over-read while parsing the group mod OpenFlow message sent from the controller

* Tue Apr 25 2017 Alexey Shabalin <shaba@altlinux.ru> 2.7.0-alt1
- 2.7.0
- build python3 package
- add ovn packages

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Thu Mar 03 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Fri Oct 02 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- build branch-2.4

* Tue Feb 03 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- build branch-2.3
- add systemd unit
- drop controller, ovsdbmonitor packages
- add vtep and devel packages
- build with --disable-static and --enable-shared
- fixed link shared libs
- backport upstream patches for devel package

* Fri Dec 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.1-alt2
- Add OVS_REMOVE and remove ports and bridges ony if set yes

* Wed Dec 25 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.1-alt1
- Fix runtimedir
- Add %_datadir/%name/scripts/ovs-check-dead-ifs
- Add etcnet support
- Fix initscript for etcnet support

* Sat Dec 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0-alt1
- 2.0
- Remove package brcompat (from upstream v1.10.0)
- Add packages ovsdbmonitor and python-module-openvswitch

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 1.4.1-alt1
- 1.4.1

* Wed Feb 22 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt2
- debugtools subpackage made noarch, optional, and off by default
  (until python part is there)

* Tue Feb 21 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- built for ALT Linux (based on openSUSE 1.2.1-1 spec)
- split into subpackages (largely inspired by debian 1.2.1-3 ones)
- neglected python-related parts for now
- *heavy* spec cleanup, buildreq
- NB: you will need kernel-modules-openvswitch (or linux-3.3+)
