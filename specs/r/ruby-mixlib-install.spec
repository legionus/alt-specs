%define  pkgname mixlib-install

Name:    ruby-%pkgname
Version: 3.11.7
Release: alt1

Summary: A library for interacting with Chef Software Inc's software distribution systems.
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/chef/mixlib-install

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires \,^/usr/sbin/installer$,d

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/%pkgname
%ruby_sitelibdir/*
%rubygem_specdir/*.gemspec

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.7-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.6-alt1
- New version.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.1-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1
- New version.
- Package as gem.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 3.10.0-alt1
- Initial build for Sisyphus
