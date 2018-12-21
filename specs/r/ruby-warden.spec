# vim: set ft=spec: -*- rpm-spec -*-

%define plugname warden

Name: ruby-%plugname
Version: 0.9.4
Release: alt2.2

Summary: General Rack Authentication Framework
License: Unspecified
Group: Development/Ruby
Url: http://wiki.github.com/hassox/warden/

BuildArch: noarch
Source: %name-%version.tar

# Automatically added by buildreq on Fri Feb 26 2010 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Warden is rack based middleware, designed to provide a mechanism for
authentication in Ruby web applications. It is a common mechanism that fits into
the Rack Machinery to offer powerful options for authentication.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc README.textile History.rdoc TODO.textile
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/Warden

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt2.2
- Rebuild with new Ruby autorequirements.

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.9.4-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 02 2010 Timur Batyrshin <erthad@altlinux.org> 0.9.4-alt2
- added README.alt

* Wed Feb 24 2010 Timur Batyrshin <erthad@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus


