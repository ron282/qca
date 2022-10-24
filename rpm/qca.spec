Name:           qca
Summary:        QCA provides a straightforward and cross-platform crypto API
Version:        2.3.4
Release:        1
License:        Lesser GNU General Public License
URL:            https://github.com/KDE/qca
Source0:        https://invent.kde.org/libraries/qca/-/archive/v2.3.4/qca-v2.3.4.tar.gz

Requires:  ca-certificates
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  cmake
BuildRequires:  ca-certificates

%description
The Qt Cryptographic Architecture (QCA) provides a straightforward and cross-
platform API for a range of cryptographic features, including SSL/TLS,
X.509 certificates, SASL, OpenPGP, S/MIME CMS, and smart cards.

%package devel
Summary:    Development package of %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
Contains files needed to development with %{name}.

%prep
%setup -q -n %{name}-%{version}/qca

%build
mkdir -p build
pushd build

%cmake .. \
  -D BUILD_TESTS:BOOL=OFF 

%make_build 
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%doc README TODO
%license COPYING
%{_libdir}/qt5/bin/qcatool-qt5
%{_libdir}/qt5/bin/mozcerts-qt5
%{_libdir}/libqca-qt5.so.*
%{_libdir}/qt5/plugins/crypto/*
%{_datadir}/qt5/man/*/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qca-qt5/QtCrypto
%{_libdir}/libqca-qt5.so
%{_libdir}/pkgconfig/qca2-qt5.pc
%{_libdir}/cmake/*/*
%{_datadir}/qt5/mkspecs/features/crypto.prf
