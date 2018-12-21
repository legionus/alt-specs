%set_verify_elf_method textrel=relaxed

Name: ocaml-ocamlnet
Version: 4.1.6
Release: alt3
Summary: Network protocols for OCaml
License: BSD
Group: Development/ML

Url: http://projects.camlcity.org/projects/ocamlnet.html
# https://gitlab.camlcity.org/gerd/lib-ocamlnet3.git
Source0:%name-%version.tar

BuildPreReq: /dev/shm
BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-camlp4-devel
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-lablgtk-devel
BuildRequires: ocaml-labltk
BuildRequires: ocaml-pcre-devel
BuildRequires: ocaml-zip-devel
BuildRequires: libgnutls-devel libnettle-devel
BuildRequires: libkrb5-devel
BuildRequires: libncurses-devel
BuildRequires: tcl-devel

%global __ocaml_requires_opts -i Asttypes -i Outcometree -i Parsetree

%description
Ocamlnet is an ongoing effort to collect modules, classes and
functions that are useful to implement network protocols. Since
version 2.2, Ocamlnet incorporates the Equeue, RPC, and Netclient
libraries, so it now really a big player.

In detail, the following features are available:

 * netstring is about processing strings that occur in network
   context. Features: MIME encoding/decoding, Date/time parsing,
   Character encoding conversion, HTML parsing and printing, URL
   parsing and printing, OO-representation of channels, and a lot
   more.

 * netcgi2 focuses on portable web applications.

 * rpc implements ONCRPC (alias SunRPC), the remote procedure call
   technology behind NFS and other Unix services.

 * netplex is a generic server framework. It can be used to build
   stand-alone server programs from individual components like those
   from netcgi2, nethttpd, and rpc.

 * netclient implements clients for HTTP (version 1.1, of course), FTP
   (currently partially), and Telnet.

 * equeue is an event queue used for many protocol implementations. It
   makes it possible to run several clients and/or servers in parallel
   without having to use multi-threading or multi-processing.

 * shell is about calling external commands like a Unix shell does.

 * netshm provides shared memory for IPC purposes.

 * netsys contains bindings for system functions missing in core OCaml.

 * netsmtp and netpop are client implementations of the SMTP and POP3
   protocols.

 * Bindings for GnuTLS and GSSAPI (TLS/HTTPS support).

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%package nethttpd
Summary: Ocamlnet HTTP daemon
License: GPLv2+
Requires: %name = %version-%release
Group: Development/ML

%description nethttpd
Nethttpd is a web server component (HTTP server implementation). It
can be used for web applications without using an extra web server, or
for serving web services.

%package nethttpd-devel
Summary: Development files for %name-nethttpd
License: GPLv2+
Requires: %name-nethttpd = %version-%release
Group: Development/ML

%description nethttpd-devel
The %name-nethttpd-devel package contains libraries and signature
files for developing applications that use %name-nethttpd.

%prep
%setup

%build
./configure \
  -bindir %_bindir \
  -datadir %_datadir/%name \
  -disable-apache \
  -enable-pcre \
  -enable-gtk2 \
  -enable-gnutls \
  -enable-gssapi \
  -enable-nethttpd \
  -enable-tcl \
  -enable-zip

make all
make opt

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

# rpc-generator/dummy.mli is empty and according to Gerd Stolpmann can
# be deleted safely.  This avoids an rpmlint warning.
rm -f $RPM_BUILD_ROOT%_libdir/ocaml/rpc-generator/dummy.mli

# NB. Do NOT strip the binaries and prevent prelink from stripping them too.
# See comment at top of spec file.
mkdir -p $RPM_BUILD_ROOT/etc/prelink.conf.d
echo -e '-b /usr/bin/netplex-admin\n-b /usr/bin/ocamlrpcgen' \
  > $RPM_BUILD_ROOT/etc/prelink.conf.d/ocaml-ocamlnet.conf

%files
%doc ChangeLog RELNOTES
%_libdir/ocaml/equeue
%_libdir/ocaml/equeue-gtk2
%_libdir/ocaml/equeue-tcl
%_libdir/ocaml/netcamlbox
%_libdir/ocaml/netcgi2
%_libdir/ocaml/netcgi2-plex
%_libdir/ocaml/netclient
%_libdir/ocaml/netgss-system
%_libdir/ocaml/netmulticore
%_libdir/ocaml/netplex
%_libdir/ocaml/netshm
%_libdir/ocaml/netstring
%_libdir/ocaml/netstring-pcre
%_libdir/ocaml/netsys
%_libdir/ocaml/nettls-gnutls
%_libdir/ocaml/netunidata
%_libdir/ocaml/netzip
%_libdir/ocaml/rpc
%_libdir/ocaml/rpc-auth-local
%_libdir/ocaml/rpc-generator
%_libdir/ocaml/shell
%exclude %_libdir/ocaml/*/*.a
%exclude %_libdir/ocaml/*/*.cmxa
%exclude %_libdir/ocaml/*/*.cmx
%exclude %_libdir/ocaml/*/*.o
%exclude %_libdir/ocaml/*/*.mli
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner
%_datadir/%name/
%_bindir/netplex-admin
%_bindir/ocamlrpcgen
%config(noreplace) /etc/prelink.conf.d/ocaml-ocamlnet.conf

%files devel
%doc ChangeLog RELNOTES
%_libdir/ocaml/*/*.a
%_libdir/ocaml/*/*.cmxa
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.o
%_libdir/ocaml/*/*.mli
%exclude %_libdir/ocaml/nethttpd/*

%files nethttpd
%doc ChangeLog RELNOTES
%_libdir/ocaml/nethttpd
%exclude %_libdir/ocaml/nethttpd/*.a
%exclude %_libdir/ocaml/nethttpd/*.cmxa
%exclude %_libdir/ocaml/nethttpd/*.mli

%files nethttpd-devel
%doc ChangeLog RELNOTES
%_libdir/ocaml/nethttpd/*.a
%_libdir/ocaml/nethttpd/*.cmxa
%_libdir/ocaml/nethttpd/*.mli

%changelog
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 4.1.6-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 4.1.6-alt2
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 4.1.6-alt1
- 4.1.6

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 4.1.2-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 4.1.2-alt2
- rebuild with ocaml 4.04.1

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 4.1.2-alt1
- first build for ALT, based on RH spec
