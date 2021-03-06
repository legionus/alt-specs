%define  pkgname audited

Name:    ruby-%pkgname
Version: 4.8.0
Release: alt1

Summary: Audited (formerly acts_as_audited) is an ORM extension that logs all changes to your Rails models.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/collectiveidea/audited

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

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
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt1
- New version.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 4.7.1-alt1
- Initial build for Sisyphus
