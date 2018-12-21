# Original package name LuaSocket
%define oname luasocket
%define oversion 3.0rc1-1
%define rockspec luasocket-3.0rc1-1.rockspec
Name: lua-module-%oname
Version: 3.0rc1
Release: alt2
Summary: Network support for the Lua language
License: MIT
Group: Development/Other
Url: http://luaforge.net/projects/luasocket/
Packager: Ildar Mulyukov <ildar@altlinux.ru>
Provides: luarocks(%oname) = %version

Source: https://github.com/diegonehab/luasocket/archive/v3.0-rc1.zip
Source1: https://rocks.moonscript.org/manifests/luarocks/luasocket-3.0rc1-1.rockspec

BuildPreReq: rpm-macros-lua >= 1.2
# Automatically added by buildreq on ...
BuildRequires: liblua5-devel luarocks unzip

%description
      LuaSocket is a Lua extension library that is composed by two parts: a C core
      that provides support for the TCP and UDP transport layers, and a set of Lua
      modules that add support for functionality commonly needed by applications
      that deal with the Internet.

%prep
%setup -n %oname-3.0-rc1

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc

%check
%lua_path_add_buildroot
( lua %buildroot%luarocks_dbdir/%oname/%oversion/test/testsrvr.lua ||: )&
sleep 1
lua %buildroot%luarocks_dbdir/%oname/%oversion/test/testclnt.lua

%files
%lua_modulesdir/*
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc FIX LICENSE* NEW TODO WISH docs_from_rockstree/*
%exclude %luarocks_dbdir/manifest

%changelog
* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0rc1-alt2
- Rebuild with new luarocks and lua-5.3

* Tue Oct 07 2014 Ildar Mulyukov <ildar@altlinux.ru> 3.0rc1-alt1_lr1
- autogenerated by lrimport

* Thu Jan 06 2011 Ildar Mulyukov <ildar@altlinux.ru> 2.0.2-alt1_lr3
- autogenerated by lrimport
