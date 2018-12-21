%define _unpackaged_files_terminate_build 1
%define  pkgname puppetserver-ca-cli

Name:    ruby-%pkgname
Version: 1.1.3
Release: alt1

Summary: A simple Ruby CLI tool to interact with the Puppet Server's included CA
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/puppetlabs/puppetserver-ca-cli

BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

Requires: ruby-bundler


%description
This gem provides the functionality behind the Puppet Server CA interactions.
The actual CLI executable lives within the Puppet Server project.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%doc README* LICENSE
%ruby_sitelibdir/*
%rubygem_specdir/*

%exclude %_bindir/*


%changelog
* Thu Dec 06 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus
