%define  pkgname citrus

Name:    ruby-%pkgname
Version: 3.0.2
Release: alt1.1

Summary: Parsing Expressions for Ruby
License: MIT or Ruby
Group:   Development/Ruby
Url:     https://github.com/mjackson/citrus

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Citrus is a compact and powerful parsing library for Ruby that combines
the elegance and expressiveness of the language with the simplicity and
power of parsing expressions.

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
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus
