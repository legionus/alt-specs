Name: pam_mkuser
Version: 0.1.0
Release: alt5

Summary: A pluggable authentication module that adds the new user account if it doesn\'t exist
License: GPLv2+
Group: System/Base
Url: http://git.altlinux.org/gears/p/pam_mkuser.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-pam
BuildRequires: rpm-build >= 0:4.0.4-alt55
BuildRequires: docbook-dtds docbook-style-xsl xsltproc
BuildRequires: libpam-devel

%define pam_name %{make_pam_name mkuser}

%description
A pluggable authentication module that adds the new user account if it
doesn\'t exist.

%package -n %pam_name
Summary: A pluggable authentication module that adds the new user account if it doesn\'t exist
License: GPLv2+
Group: System/Base
Provides: %name = %version-%release

Requires: shadow-utils

%description -n %pam_name
A pluggable authentication module that adds the new user account if it
doesn\'t exist.

%prep
%setup

%build
%autoreconf
%configure \
	--libdir=/%_lib \
	--sbindir=%_sbindir \
	--includedir=%_includedir/security

%make_build

%install
%makeinstall_std

%find_lang %name

%files -n %pam_name -f %name.lang
%_pam_modules_dir/*
%_mandir/man*/*.*
%_controldir/*

%changelog
* Wed Aug 22 2018 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt5
- Rebuild the package to make it available for the "aarch64" arch.

* Fri Jul 28 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt4
- Fix: Resolve the links because sed -i replaces the files.

* Fri Jul 28 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt3
- Provide the versioned "pam_mkuser" name.

* Fri Jul 21 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Add pam_mkuser on/off control script.

* Wed Jul 12 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial version.
