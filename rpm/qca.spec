Name:           qca
Summary:        QCA provides a straightforward and cross-platform crypto API
Version:        2.3.4
Release:        1
License:        Lesser GNU General Public License
URL:            https://github.com/KDE/qca
Source0:        https://invent.kde.org/libraries/qca/-/archive/v2.3.4/qca-v2.3.4.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description

%package devel
Summary:    Development package of %{name}
Requires:   %{name} = %{version}
Provides:		%{name}-devel

%description devel
Contains files needed to development with %{name}.

%prep
#%autosetup -p1 -n %{name}-%{version}/%{name}

%build
mkdir -p build
pushd build

%cmake .. \
  -D QCA_BINARY_INSTALL_DIR:STRING=%{_bindir} \
  -D QCA_FEATURE_INSTALL_DIR:PATH=%{_qt5_prefix}/mkspecs/features \
  -D QCA_INCLUDE_INSTALL_DIR:PATH=%{_qt5_headerdir} \
  -D QCA_LIBRARY_INSTALL_DIR:PATH=%{_qt5_libdir} \
  -D QCA_PLUGINS_INSTALL_DIR:PATH=%{_qt5_plugindir} \
  -D QCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{_qt5_headerdir} \
  -D BUILD_TESTS=OFF \
  -D BUILD_SHARED_LIBS=FALSE \
  -D BUILD_PLUGINS=NONE

%make_build 
popd

%install
pushd build
%make_install
cp -Ra lib/lib%{name}-qt5.a %{buildroot}%{_libdir}
popd

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files 
%doc README TODO
%license COPYING
%{_bindir}/mozcerts-qt5
%{_bindir}/qcatool-qt5
%{_mandir}/man1/qcatool-qt5.1*
 
%files devel
%{_qt5_headerdir}/QtCrypto
%{_libdir}/pkgconfig/qca2-qt5.pc
%{_libdir}/cmake/Qca-qt5/
%{_libdir}/libqca-qt5.a
%{_qt5_prefix}/mkspecs/features/crypto.prf
