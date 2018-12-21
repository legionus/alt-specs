%define  pkgname inflection

Name: 	 ruby-%pkgname
Version: 1.0.0 
Release: alt1.1

Summary: Provides english inflection
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/reactormonk/extlib/tree/inflection

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Support library for inflections.

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
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build in Sisyphus
