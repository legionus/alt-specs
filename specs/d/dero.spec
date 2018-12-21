Name:		dero
Version:	0.11.1.0
Release:	alt1.2
Summary:	Dero Wallet
Url:		http://dero.io
Group:		Office
License:	MIT
Source0:	%name.tar.xz

Patch1: dero-alt-boost-compat.patch

# Automatically added by buildreq on Tue Feb 06 2018 (-bi)
# optimized out: boost-devel boost-devel-headers cmake-modules elfutils libcom_err-devel libkrb5-devel libstdc++-devel perl pkg-config python-base python-modules python3 python3-base rpm-build-python3 xz
BuildRequires: boost-asio-devel boost-filesystem-devel boost-interprocess-devel boost-program_options-devel cmake doxygen gcc-c++ glibc-devel-static libevent-devel libminiupnpc-devel libreadline-devel libssl-devel

%description
DERO is a fork of Monero (Helium Hydra), Utilizing CryptoNote protocol.
DERO aims be a completely new blockchain technology, integrating cryptonote
protocol features for privacy and also new smart contract control.
Cryptonote core is in the process of updates in golang. DERO will be
introducing smart contracts on to our blockchain.

%prep
%setup -n %name
%patch1 -p2

%build
mkdir ./build && cd ./build
cmake 			../. \
			-DCMAKE_CXX_FLAGS='%optflags' \
			-DCMAKE_INSTALL_PREFIX=/usr
%make_build

%install
cd ./build
make DESTDIR=%buildroot install

%files
%doc CONTRIBUTING.md LICENSE README.i18n.md README.md VULNERABILITY_RESPONSE_PROCESS.md
%_bindir/*

%changelog
* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.11.1.0-alt1.2
- NMU: Rebuild with new openssl 1.1.0.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.1.0-alt1.1
- NMU: rebuilt with boost-1.67.0

* Tue Feb 06 2018 Motsyo Gennadi <drool@altlinux.ru> 0.11.1.0-alt1
- initial build for ALT Linux
