%define  pkgname turbolinks

Name:    ruby-%pkgname
Version: 2.5.4
Release: alt2
Epoch:   1

Summary: Turbolinks makes navigating your web application faster
License: MIT
Group:   Development/Ruby
Url:     https://github.com/turbolinks/turbolinks

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Turbolinks(r) makes navigating your web application faster. Get the
performance benefits of a single-page application without the added
complexity of a client-side JavaScript framework. Use HTML to render
your views on the server side and link to pages as usual. When you
follow a link, Turbolinks automatically fetches the page, swaps in its
<body>, and merges its <head>, all without incurring the cost of a full
page load.

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
* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 1:2.5.4-alt2
- Added new epoch.

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.4-alt1
- Downgrade to 2.5.4 for foreman.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Fri Jul 27 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1.1
- Use appropriate source from https://github.com/turbolinks/turbolinks-rails.
- Rebuild with new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- Initial build for Sisyphus
