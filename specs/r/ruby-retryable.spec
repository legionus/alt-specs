%define  pkgname retryable

Name:    ruby-%pkgname
Version: 3.0.2
Release: alt1

Summary: Kernel#retryable, by Cheah Chu Yeow (http://is.gd/faW9), slightly enhanced and rebuilt as gem as a little Munich Hackday project.
License: MIT
Group:   Development/Ruby
Url:     http://github.com/nfedyashev/retryable

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
* Tue Sep 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
