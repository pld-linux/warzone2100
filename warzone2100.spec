#$Revision: 1.21.2.3 $, $Date: 2008-12-03 09:43:09 $
%define		_rc	rc2
Summary:	3D realtime strategy on a future Earth
Summary(pl.UTF-8):	Gra RTS, której akcja toczy się w przyszłości
Name:		warzone2100
Version:	2.1
Release:	0.%{_rc}.1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://download.gna.org/warzone/releases/2.1/%{name}-%{version}_%{_rc}.tar.bz2
# Source0-md5:	bce57301df1b134898890e55a806948e
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-configure.patch
URL:		http://www.wz2100.net/
BuildRequires:	OpenAL-devel >= 0.0.8
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	libvorbis-devel >= 1.1
BuildRequires:	perl-base
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	quesoglc-devel
BuildRequires:	unzip
BuildRequires:	zip
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
%setup -q -n %{name}-%{version}_%{_rc}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
#%{__perl} -pi -e "s#-m32##g" makerules/common.mk
%{__perl} -pi -e "s#-m32##g" configure
%configure --with-distributor="PLD"
%{__make} \
	OPENAL_LIBS="`openal-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install icons/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install icons/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.*
