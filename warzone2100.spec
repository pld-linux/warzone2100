Summary:	3D realtime strategy on a future Earth
Summary(pl.UTF-8):	Gra RTS, której akcja toczy się w przyszłości
Name:		warzone2100
Version:	3.1.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://downloads.sourceforge.net/warzone2100/%{name}-%{version}.tar.xz
# Source0-md5:	7f061f3e5a2a6a83c146508ccefabd86
URL:		http://www.wz2100.net/
BuildRequires:	OpenAL-devel >= 0.0.8-4
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	libtheora-devel >= 0.1
BuildRequires:	libvorbis-devel >= 1.1
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	quesoglc-devel
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zip
Requires:	fonts-TTF-DejaVu
Requires:	gdb
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

%prep
%setup -q

# et_EE -> et
%{__sed} -e 's/et_EE/et/g' -i po/LINGUAS
mv po/et{_EE,}.po
mv po/et{_EE,}.gmo

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-distributor="PLD" \
	--docdir=%{_docdir}/%{name}-%{version} \
	--with-icondir=%{_pixmapsdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ca_ES
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/uk_UA

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/man6/%{name}.6*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
