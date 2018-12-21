# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname stomp

Name: ruby-%pkgname
Version: 1.1.9
Release: alt1.3

Summary: Ruby client for the Stomp messaging protocol
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/stomp/

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Wed Sep 28 2011 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-setup

%description
FILL ME.

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%ruby_sitelibdir/*
%rubygem_specdir/*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1.2
- Rebuild with Ruby 2.4.1

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.1.9-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Sep 28 2011 Sergey Alembekov <rt@altlinux.ru> 1.1.9-alt1
- Built for Sisyphus

