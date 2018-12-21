%define  pkgname retriable

Name:    ruby-%pkgname
Version: 3.1.2
Release: alt3

Summary: Retriable is an simple DSL to retry failed code blocks with randomized exponential backoff.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/kamui/retriable

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
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Nov 14 2018 Pavel Skrylev <majioa@altlinux.org> 3.1.2-alt3
- Gemify correctly 3.1.2

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt2
- Rebuild for correct gemspec file name.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version.
- Package as gem.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
