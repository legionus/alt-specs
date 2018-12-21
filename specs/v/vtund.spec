%define item vtun

%define release_pre alt3

# for distr selected
%def_without M40
%def_without M41
%def_without M50
%def_without M60P

# %%distr_switch set
%define distr_switch %nil
%if_with M40
%define distr_switch M40
%endif
%if_with M41
%define distr_switch M41
%endif
%if_with M50
%define distr_switch M50
%endif
%if_with M60P
%define distr_switch M60P
%endif
%if_with M70P
%define distr_switch M70P
%endif

# %%release_num and %%release_distr set
%if "%distr_switch" == ""
%define release_distr %nil
%else
%define release_distr .%distr_switch
%endif

# %%package_release set
%define package_release %{release_pre}%{release_distr}

Name: vtund
Version: 3.0.3
Release: %package_release

Summary: Virtual tunnel over TCP/IP networks.
License: GPL
Group: System/Servers

URL: http://vtun.sourceforge.net/
Packager: Yura Kalinichenko <yuk@altlinux.org>

Source0: %item-%version.tar.gz
Source1: %name.init
Source2: %name.sysconfig
Source3: %name.client.sysconfig
Source4: %name.bug4231.sh
Source5: README.compat-2.6

Provides: vtund

# Automatically added by buildreq on Fri May 28 2004
BuildRequires: flex liblzo2-devel libssl-devel zlib-devel

%description
VTun provides the method for creating Virtual Tunnels over TCP/IP
networks and allows to shape, compress, encrypt traffic in that
tunnels.  Supported type of tunnels are: PPP, IP, Ethernet and most of
other serial protocols and programs.

VTun is easily and highly configurable: it can be used for various
network tasks like VPN, Mobil IP, Shaped Internet access, IP address
saving, etc.  It is completely a user space implementation and does
not require modification to any kernel parts.

%prep
%setup -n %item-%version
%add_optflags "-std=gnu89"
aclocal
autoconf
%configure

%build
%make_build

%install
install -d %buildroot{%_sbindir,%_libdir/%name,%_man8dir,%_man5dir,%_initdir,%_sysconfdir/sysconfig/%name}
install -pm640 vtund.conf   %buildroot%_sysconfdir
install -pm755 %SOURCE1     %buildroot%_initdir/vtund
install -pm640 %SOURCE2     %buildroot%_sysconfdir/sysconfig/vtund_server
install -pm640 %SOURCE3     %buildroot%_sysconfdir/sysconfig/%name/backup
install -pm755 %SOURCE4     %buildroot%_libdir/%name/bug4231.sh
install -pm644 %SOURCE5     .
install -pm755 vtund        %buildroot%_sbindir
install -pm644 vtund.conf.5 %buildroot%_man5dir
install -pm644 vtund.8      %buildroot%_man8dir

sed -i 's,/usr/lib,%_libdir,g' %buildroot%_initdir/vtund

%files
%doc ChangeLog Credits FAQ README README.Setup README.Shaper TODO README*
%doc TODO vtund.conf 
%config(noreplace) %_sysconfdir/vtund.conf
%config(noreplace) %_sysconfdir/sysconfig/vtund_server
%config(noreplace) %_sysconfdir/sysconfig/%name/backup
%_initdir/*
%_sbindir/*
%_libdir/%name/
%_man8dir/*
%_man5dir/*

%changelog
* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 3.0.3-alt3
- gcc5 FTBFS workaround (-std=gnu89)

* Wed Jan 28 2015 Michael Shigorin <mike@altlinux.org> 3.0.3-alt2
- NMU: fixed initscript on x86_64 (closes: #30676)
- minor spec cleanup

* Thu Aug 15 2013 Michael Shigorin <mike@altlinux.org> 3.0.3-alt1
- NMU:
  + Release 3.0.3
    - dropped vtun-3.0.2-legacy_encrypt.patch (rfe1685781 merged upstream)
  + added --with M70P support
  + minor spec cleanup (closes: #8595)

* Thu Sep  1 2011 Yura Kalinichenko <yuk@altlinux.org> 3.0.2-alt4
- vtun-3.0.2-free_host.patch cutted from vtun-3.0.2-legacy_encrypt.patch
  and not use while.
  TODO: right memory free

* Mon Aug  8 2011 Yura Kalinichenko <yuk@altlinux.ru> 3.0.2-alt3
- Included README.compat-2.6

* Wed Jul 20 2011 Yura Kalinichenko <yuk@kalina.in.ua> 3.0.2-alt1
- Release 3.0.2

* Wed Jul 20 2011 Yura Kalinichenko <yuk@kalina.in.ua> 3.0.1-alt1
- Release 3.0.1

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.6-alt3.1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.6-alt3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Tue May 27 2004 Peter V. Saveliev <peet@altlinux.ru> 2.6-alt3
- Startup script changed, so it is possible to perform an action upon
    explicit session

* Tue May 18 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 2.6-alt2
- Updated package requires
- Added changelog description

* Sun Jan 11 2004 Peter V. Saveliev <peet@altlinux.ru> 2.6-alt1
- Initial release
