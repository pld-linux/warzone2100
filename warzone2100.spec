# TODO: system 3rdparty libs (fmt, re2...)
Summary:	3D realtime strategy on a future Earth
Summary(pl.UTF-8):	Gra RTS, której akcja toczy się w przyszłości
Name:		warzone2100
Version:	4.6.1
Release:	4
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	https://downloads.sourceforge.net/warzone2100/releases/%{version}/%{name}_src.tar.xz
# Source0-md5:	500e1a169f39454789bfc6bdb66b7582
Source1:	https://downloads.sourceforge.net/project/warzone2100/warzone2100/Videos/high-quality-en/sequences.wz
# Source1-md5:	9a1ee8e8e054a0ad5ef5efb63e361bcc
Patch0:		x32.patch
URL:		https://www.wz2100.net/
BuildRequires:	OpenAL-devel >= 0.0.8-4
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	Vulkan-Headers
BuildRequires:	cmake >= 3.16
BuildRequires:	curl-devel >= 8.16.0
BuildRequires:	freetype-devel >= 2
BuildRequires:	fribidi-devel
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	harfbuzz-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	libsodium-devel >= 1.0.14
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtheora-devel >= 0.1
BuildRequires:	libvorbis-devel >= 1.1
BuildRequires:	libzip-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	opus-devel
# 7z
BuildRequires:	p7zip
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	ruby-asciidoctor >= 1.5.3
BuildRequires:	shaderc
BuildRequires:	sqlite3-devel >= 3.14
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
Requires:	fonts-TTF-DejaVu
Requires:	libsodium >= 1.0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Warzone 2100 is a real-time strategy game. Although comparable to
Earth 2150 in many significant respects, it does contain aspects that
are unique. These include various radar technologies and a greater
focus on artillery and counter-battery technologies.

%description -l pl.UTF-8
Warzone 2100 jest grą strategiczną czasu rzeczywistego. Chociaż gra
bardzo przypomina grę Earth 2150, to jednak zostało do niej
wprowadzonych kilka ciekawych pomysłów. Są to między innymi rozmaite
technologie radarowe oraz większe skupienie się na technologiach
artyleryjskich oraz obronie przeciwlotniczej.

%package data
Summary:	Warzone 2100 data files
Summary(pl.UTF-8):	Pliki danych Warzone 2100
Group:		X11/Applications/Games/Strategy
BuildArch:	noarch

%description data
Warzone 2100 data files

%description data -l pl.UTF-8
Pliki danych Warzone 2100.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%cmake -B build \
	-DBUILD_SHARED_LIBS=OFF \
	-DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}-%{version}

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{ar_SA,ar}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{bg_BG,bg}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{ca_ES,ca}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{et_EE,et}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{fa_IR,fa}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{he_IL,he}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{ja_JP,ja}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{my_MM,my}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{tt_RU,tt}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{uk_UA,uk}

%{__mv} $RPM_BUILD_ROOT{%{_iconsdir},%{_pixmapsdir}}/net.wz2100.warzone2100.png

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_desktopdir}/net.wz2100.warzone2100.desktop
%{_datadir}/metainfo/net.wz2100.warzone2100.metainfo.xml
%{_pixmapsdir}/net.wz2100.warzone2100.png

%files data
%defattr(644,root,root,755)
%{_datadir}/%{name}
