%define pypolicy_admin mailadm
%define pypolicy_owner policyd-spf

Name: pypolicyd-spf
Version: 1.3.2
Release: alt1

Summary: Postfix policy server for SPF checking

License: Apache-2.0
Group: System/Servers
Url: https://launchpad.net/pypolicyd-spf
Source: %name-%version.tar
Patch: debian-install-conf-fix.patch

Packager: L.A. Kostis <lakostis@altlinux.ru>

BuildArch: noarch

%setup_python_module %name

BuildRequires: python-module-pyspf
Requires: python-module-ipaddr
Provides: postfix-policyd-spf-python

%description
postfix-policyd-spf-python is a full featured Postfix SMTPd policy engine
for SPF checking. It includes a variety of whitelisting mechanisms and
policy options to enable it to support the widest variety of system
requirements.  It is implemented in pure Python and uses the python-spf
module.  The SPF web site is http://www.openspf.org/.

%prep
%setup -q
%patch -p1

%build
%python_build

%install
%python_install --optimize=2 --record=INSTALLED_FILES
install -m644 policyd-spf.conf.commented %buildroot%_sysconfdir/postfix-policyd-spf-python/

subst '/\/share\/man/d' INSTALLED_FILES

%pre
/usr/sbin/groupadd -r -f %pypolicy_owner
/usr/sbin/groupadd -r -f %pypolicy_admin

/usr/sbin/useradd -r -n -g %pypolicy_owner -M -s /dev/null -c %pypolicy_owner %pypolicy_owner >/dev/null 2>&1 ||:

%files -f INSTALLED_FILES
%_man1dir/*
%_man5dir/*
%dir %_sysconfdir/postfix-policyd-spf-python
%_sysconfdir/postfix-policyd-spf-python/*.commented
%exclude %python_sitelibdir/*.egg-info
%doc README* CHANGES COPYING

%changelog
* Mon Aug 31 2015 L.A. Kostis <lakostis@altlinux.ru> 1.3.2-alt1
- 1.3.2.

* Fri Aug 03 2012 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt1
- 1.1.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt0.1.1
- Rebuild with Python-2.7

* Fri Aug 26 2011 L.A. Kostis <lakostis@altlinux.ru> 0.8.1-alt0.1
- Initial build for ALTLinux.
