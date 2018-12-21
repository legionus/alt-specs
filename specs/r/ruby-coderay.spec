%define  pkgname coderay

Name: 	 ruby-%pkgname
Version: 1.1.2
Release: alt1.1

Summary: Fast and easy syntax highlighting for selected languages, written in Ruby
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rubychan/coderay

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
CodeRay is a Ruby library for syntax highlighting.

You put your code in, and you get it back colored; Keywords, strings, floats,
comments - all in different colors. And with line numbers.

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
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Sat Oct 21 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.2-alt1
- new version 1.1.2

* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.1.1-alt1
- Initial build in Sisyphus
