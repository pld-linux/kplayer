Summary:	KDE media player based on mplayer
Summary(pl):	Odtwarzacz mediów dla KDE bazuj±cy na mplayerze
Name:		kplayer
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kplayer/%{name}-%{version}.tar.bz2
# Source0-md5:	c04b7a2a8c5d169d6c7c9c445da7c837
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-am110.patch
URL:		http://kplayer.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.3
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPlayer is a KDE media player based on mplayer.

%description -l pl
KPlayer to odtwarzacz mediów dla KDE bazuj±cy na mplayerze.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	applnkdir=%{_desktopdir} \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kplayer
%{_libdir}/kde3/libkplayerpart.la
%attr(755,root,root) %{_libdir}/kde3/libkplayerpart.so
%{_datadir}/apps/kplayer
%{_datadir}/services/kplayerpart.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_desktopdir}/kde/kplayer.desktop
%{_datadir}/apps/konqueror/servicemenus/kplayer-*.desktop
