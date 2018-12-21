%define  pkgname metaclass

Name:    ruby-%pkgname
Version: 0.0.4
Release: alt1.1

Summary: Adds a metaclass method to all Ruby objects
License: MIT
Group:   Development/Ruby
Url:     https://github.com/floehopper/metaclass

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Adds a __metaclass__ method to all Ruby objects.

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

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Aug 20 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.4-alt1
- Initial build for Sisyphus
