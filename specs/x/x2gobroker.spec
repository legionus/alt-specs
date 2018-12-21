Name: x2gobroker
Version: 0.0.3.4
Release: alt2
Summary: X2Go Session Broker
License: AGPLv3+
Group: Communications
Url: http://www.x2go.org/

Packager: Oleg Solovyov <mcpain@altlinux.org>

Source: http://code.x2go.org/releases/source/%name/%name-%version.tar.gz

# Automatically added by buildreq on Tue Dec 04 2018 (-bi)
# optimized out: bash3 bashrc elfutils perl python-base python-module-pkg_resources python-modules python-modules-compiler python-modules-ctypes python-modules-distutils python-modules-email python-modules-encodings sh3 xz
BuildRequires: perl-File-Which python-module-setuptools

BuildRequires: python-module-setuptools
BuildRequires: perl-File-Which
Requires(pre):  python-module-x2gobroker = %version-%release
Requires(pre):  shadow-utils

%description
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

The session broker is a server tool for X2Go that tells your X2Go Client
application in a terminal server cluster what servers and session types are
most appropriate for the user in front of the X2Go terminal.

A session broker is most useful in load balanced X2Go server farms.

This package contains the x2gobroker executable.

%package -n python-module-x2gobroker
Summary: X2Go Session Broker (Python modules)
Group: Communications
BuildArch: noarch

%description -n python-module-x2gobroker
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

The session broker is a server tool for X2Go that tells your X2Go Client
application in a terminal server cluster what servers and session types are
most appropriate for the user in front of the X2Go terminal.

A session broker is most useful in load balanced X2Go server farms.

This package contains the broker's Python library.

%package authservice
Summary: X2Go Session Broker (PAM authentication service)
Group: Communications
BuildArch: noarch
Requires(pre): python-module-x2gobroker = %version-%release

%description authservice
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

The session broker is a server tool for X2Go that tells your X2Go Client
application in a terminal server cluster what servers and session types are
most appropriate for the user in front of the X2Go terminal.

A session broker is most useful in load balanced X2Go server farms.

This package contains the authentication service against the PAM system.

%package loadchecker
Summary: X2Go Session Broker (load checker service)
Group: Communications
BuildArch: noarch
Requires(pre): python-module-x2gobroker = %version-%release

%description loadchecker
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

The session broker is a server tool for X2Go that tells your X2Go Client
application in a terminal server cluster what servers and session types are
most appropriate for the user in front of the X2Go terminal.

A session broker is most useful in load balanced X2Go server farms.

This package contains the load checker service required for broker setups
with dynamic load balancing.

%package daemon
Summary: X2Go Session Broker (standalone daemon)
Group: Communications
BuildArch: noarch
Requires: x2gobroker = %version-%release
Requires: x2gobroker-authservice = %version-%release

%description daemon
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

The session broker is a server tool for X2Go that tells your X2Go Client
application in a terminal server cluster what servers and session types are
most appropriate for the user in front of the X2Go terminal.

A session broker is most useful in load balanced X2Go server farms.

This package contains the start-stop script that installs the X2Go Session Broker
as standalone daemon.

%package ssh
Summary: X2Go Session Broker (SSH broker)
Group: Communications
Requires: x2gobroker = %version-%release

%description ssh
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

The session broker is a server tool for X2Go that tells your X2Go Client
application in a terminal server cluster what servers and session types are
most appropriate for the user in front of the X2Go terminal.

A session broker is most useful in load balanced X2Go server farms.

This add-on package provides fully-featured SSH brokerage support (with access
to broker agents on remote X2Go servers).

%package wsgi
Summary: X2Go Session Broker (WSGI)
Group: Communications
BuildArch: noarch
Requires: x2gobroker = %version-%release
Requires: x2gobroker-authservice = %version-%release

%description wsgi
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

The session broker is a server tool for X2Go that tells your X2Go Client
application in a terminal server cluster what servers and session types are
most appropriate for the user in front of the X2Go terminal.

A session broker is most useful in load balanced X2Go server farms.

This package contains an Apache2 configuration that installs the X2Go Session
Broker as a WSGI application into a running Apache2 httpd.

%package agent
Summary: X2Go Session Broker (remote agent)
Group: Communications

%description agent
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

The session broker is a server tool for X2Go that tells your X2Go Client
application in a terminal server cluster what servers and session types are
most appropriate for the user in front of the X2Go terminal.

A session broker is most useful in load balanced X2Go server farms.

This package contains a setuid agent command that extends X2Go Session Broker
functionality. It has to be installed on X2Go Servers that shall be
controlled via a session broker.

The broker agent provides means to the X2Go Session Broker for controlling
the X2Go Server it is installed on (e.g. suspend/terminate sessions, deploy
SSH login keys, detect server load, detect running/suspended sessions
of connecting users, etc.).

WARNING: This package installs a setuid wrapper
(%_libdir/x2go/broker/x2gobroker-agent) on your system. This setuid wrapper
aims to be a secure replacement for the deprecated suidperl exectuable that
was removed from Perl (>= 5.12).

This wrapper is only able to execute the Perl script
%_libdir/x2go/broker/x2gobroker-agent.pl. For running properly,
x2gobroker-agent.pl needs setuid root privileges.

If you hesitate to install this package, study the code of the named wrapper
and the named Perl script beforehand. Note that the X2Go session broker will
lack functionality, but it will work without this x2gobroker-agent component
installed on your to-be-managed X2Go servers.

%prep
%setup

%build
echo "Files where we will be patching libexecedir:"
find . -type f -exec grep -l "/usr/lib/x2go/" "{}" "+"
find . -type f -exec grep -l "/usr/lib/x2go/" "{}" "+" | \
	xargs perl -i -pe 's{/usr/lib/x2go/}{%_libexecdir/x2go/}'

grep -l -r -E '^#!%_bindir/env python$' | while read file; do \
    sed -i "$file" \
        -e 's#%_bindir/env python#%_bindir/env python2#'
done

sed -i logrotate/x2gobroker-authservice \
    -e 's/adm/root/'
sed -i logrotate/x2gobroker-loadchecker \
    -e 's/adm/root/'
sed -i logrotate/x2gobroker-daemon \
    -e 's/adm/root/'
sed -i logrotate/x2gobroker-wsgi \
    -e 's/adm/root/'
%make_build PREFIX="%prefix" LIBDIR="%_libdir/x2go"

%install
%make_install install PREFIX="%prefix" LIBDIR="%_libdir/x2go" DESTDIR="%buildroot"

mkdir -p "%buildroot/%_sysconfdir/apache2"/{conf.d,vhosts.d}
ln -s "%_sysconfdir/x2go/x2gobroker-wsgi.apache.conf" \
	"%buildroot/%_sysconfdir/apache2/conf.d/x2gobroker-wsgi.conf"
ln -s "%_sysconfdir/x2go/x2gobroker-wsgi.apache.vhost" \
	"%buildroot/%_sysconfdir/apache2/vhosts.d/x2gobroker-wsgi.sample"

# System.d session cleanup script
mkdir -p %buildroot%_unitdir
install -pm0644 x2gobroker-daemon.service %buildroot%_unitdir
install -pm0644 x2gobroker-authservice.service %buildroot%_unitdir
install -pm0644 x2gobroker-loadchecker.service %buildroot%_unitdir

%pre -n python-module-x2gobroker
if ! %_bindir/getent group x2gobroker 1>/dev/null 2>/dev/null && %_sbindir/groupadd -r x2gobroker; then
	if ! %_bindir/getent passwd x2gobroker 1>/dev/null 2>/dev/null; then
		%_sbindir/useradd -c "X2Go Broker System User" \
		    -d "%_sharedstatedir/x2gobroker" \
		    -g x2gobroker -r -s /bin/bash x2gobroker || :
	fi
fi

%post authservice
%post_service x2gobroker-authservice

%preun authservice
%preun_service x2gobroker-authservice

%post loadchecker
%post_service x2gobroker-loadchecker

%preun loadchecker
%preun_service x2gobroker-loadchecker

%post daemon
%post_service x2gobroker-daemon

%preun daemon
%preun_service x2gobroker-daemon

%post ssh
if ! %_bindir/getent group x2gobroker-users 1>/dev/null 2>/dev/null; then
	%_sbindir/groupadd -r x2gobroker-users
fi

%pre agent
if ! %_bindir/getent group x2gobroker 1>/dev/null 2>/dev/null && %_sbindir/groupadd -r x2gobroker; then
	if ! %_bindir/getent passwd x2gobroker 1>/dev/null 2>/dev/null; then
		%_sbindir/useradd -c "X2Go Broker System User" \
		    -d "%_sharedstatedir/x2gobroker" \
		    -g x2gobroker -r -s /bin/bash x2gobroker || :
	fi
fi

%files
%_bindir/x2gobroker
%_bindir/x2gobroker-testauth
%_sbindir/x2gobroker-keygen
%_sbindir/x2gobroker-testagent
%_man1dir/x2gobroker*.1*
%exclude %_man1dir/x2gobroker-ssh.1*
%exclude %_man1dir/x2gobroker-daemon.1*
%_man8dir/x2gobroker-keygen.8*
%_man8dir/x2gobroker-testagent.8*
%attr(02750,x2gobroker,x2gobroker) %_logdir/x2gobroker
%attr(00750,x2gobroker,x2gobroker) %_sharedstatedir/x2gobroker

%files -n python-module-x2gobroker
%config(noreplace) %_sysconfdir/x2go
%exclude %_sysconfdir/x2go/x2gobroker-wsgi.apache.conf
%exclude %_sysconfdir/x2go/x2gobroker-wsgi.apache.vhost
%config %_sysconfdir/pam.d/*
%config %_sysconfdir/default/python-x2gobroker
%python_sitelibdir_noarch/x2gobroker*

%files authservice
%_unitdir/x2gobroker-authservice.service
%config %_logrotatedir/x2gobroker-authservice
%config %_sysconfdir/default/x2gobroker-authservice
%_sbindir/x2gobroker-authservice
%_man8dir/x2gobroker-authservice.8*

%files loadchecker
%_unitdir/x2gobroker-loadchecker.service
%config %_sysconfdir/default/x2gobroker-loadchecker
%config %_logrotatedir/x2gobroker-loadchecker
%_sbindir/x2gobroker-loadchecker
%_man8dir/x2gobroker-loadchecker.8*

%files daemon
%_bindir/x2gobroker-daemon
%_unitdir/x2gobroker-daemon.service
%_sbindir/x2gobroker-daemon-debug
%_man1dir/x2gobroker-daemon.1*
%_man8dir/x2gobroker-daemon-debug.8*
%config %_logrotatedir/x2gobroker-daemon
%config %_sysconfdir/default/x2gobroker-daemon

%files ssh
%attr(04510,x2gobroker,x2gobroker-users) %_bindir/x2gobroker-ssh
%_man1dir/x2gobroker-ssh.1*
%_sysconfdir/sudoers.d/x2gobroker-ssh

%files wsgi
%_sysconfdir/apache2
%config %_sysconfdir/x2go/x2gobroker-wsgi.apache.conf
%config %_sysconfdir/x2go/x2gobroker-wsgi.apache.vhost
%config %_logrotatedir/x2gobroker-wsgi

%files agent
%attr(04710,root,x2gobroker) %_libdir/x2go/x2gobroker-agent
%_libdir/x2go/x2gobroker-agent.pl
%_sbindir/x2gobroker-pubkeyauthorizer
%_man8dir/x2gobroker-pubkeyauthorizer.8*

%changelog
* Thu Dec 13 2018 Oleg Solovyov <mcpain@altlinux.org> 0.0.3.4-alt2
- fix files

* Fri Nov 30 2018 Oleg Solovyov <mcpain@altlinux.org> 0.0.3.4-alt1
- initial build for ALT Sisyphus

