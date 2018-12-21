%define  pkgname spawn-for-legacy

Name:    ruby-sfl
Version: 2.1
Release: alt1.1

Summary: spawn! spawn! spawn! spawn! spawn! spawn!
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/ujihisa/spawn-for-legacy

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

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
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.1-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 2.1-alt1
- Initial build for Sisyphus
