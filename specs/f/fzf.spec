%global import_path github.com/junegunn/fzf
%global commit b46227dcb6f1718d66ad828443d9f03a4bd58c4c
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:		fzf
Version:	0.17.5
Release:	alt1
Summary:	A general-purpose command-line fuzzy finder.

Group:		Development/Tools
License:	MIT
URL:		https://%import_path

Packager:	Vladimir Didenko <cow@altlinux.org>

Source0: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): rpm-build-vim
BuildRequires: golang
BuildRequires: golang(github.com/gdamore/tcell)
BuildRequires: golang(github.com/gdamore/tcell/encoding)
BuildRequires: golang(github.com/mattn/go-isatty)
BuildRequires: golang(github.com/mattn/go-runewidth)
BuildRequires: golang(github.com/mattn/go-shellwords)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)

%description
fzf is an interactive Unix filter for command-line that can be used with any
list; files, command history, processes, hostnames, bookmarks, git commits, etc.

%package tmux
Summary: script for launching fzf in a tmux pane
Group: Development/Tools
BuildArch: noarch

%description tmux
Script for launching fzf in a tmux pane

%package -n bash-completion-%name
Summary: Bash completion for %name
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: %name = %EVR

%description -n bash-completion-%name
Bash completion for %name.

%package -n zsh-completion-%name
Summary: Zsh completion for %name
Group: Shells
BuildArch: noarch
Requires: %name = %EVR

%description -n zsh-completion-%name
Zsh completion for %name.

%package -n vim-plugin-%name
Summary: Vim plugin for %name
Group: Editors
BuildArch: noarch
Requires: %_bindir/vim
Requires: %name = %EVR

%description -n vim-plugin-%name
Vim plugin for %name

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

# install main binary
%golang_install

#install tmux support
install -Dpm0755 bin/%name-tmux %{buildroot}%{_bindir}/

#install man pages
install -d -p %{buildroot}%{_mandir}/man1
install -Dpm0644 man/man1/*.1 %{buildroot}%{_mandir}/man1/

install -d %{buildroot}%{_datadir}/%name/shell
install -Dpm0644 shell/key-bindings.* %{buildroot}%{_datadir}/%name/shell/

# Install shell completion
install -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -Dpm0644 shell/completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/fzf
install -d %{buildroot}%{_datadir}/zsh/site-functions
install -Dpm0644 shell/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/fzf

# Install vim plugin
install -d %buildroot%vim_runtime_dir/plugin
install -Dpm0644 plugin/fzf.vim %buildroot%vim_runtime_dir/plugin/

%files
%_bindir/%name
%_mandir/man1/%name.1*
%dir %_datadir/%name
%_datadir/%name/shell

%files tmux
%_bindir/%name-tmux
%{_mandir}/man1/%name-tmux.1*

%files -n bash-completion-%name
%_sysconfdir/bash_completion.d/*

%files -n zsh-completion-%name
%_datadir/zsh/site-functions/*

%files -n vim-plugin-%name
%vim_runtime_dir/plugin/*

%changelog
* Wed Oct 24 2018 Vladimir Didenko <cow@altlinux.org> 0.17.5-alt1
- New version

* Fri Jul 27 2018 Vladimir Didenko <cow@altlinux.org> 0.17.4-alt1
- Initial build for Sisyphus
