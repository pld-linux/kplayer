Summary:	KDE media player based on mplayer
Summary(pl):	Odtwarzacz mediów dla KDE bazuj±cy na mplayerze
Name:		kplayer
Version:	0.5.3
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kplayer/%{name}-%{version}.tar.bz2
# Source0-md5:	ea7398f96efa2f01ac875c548ab01878
Patch0:		%{name}-desktop.patch
URL:		http://kplayer.sourceforge.net/	
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdelibs >= 9:3.3.0-2
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPlayer is a KDE media player based on mplayer.

%description -l pl
KPlayer to odtwarzacz mediów dla KDE bazuj±cy na mplayerze.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	applnkdir=%{_desktopdir}

# included in kdelibs
rm -f $RPM_BUILD_ROOT%{_datadir}/services/{mms,rtsp}.protocol

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kplayer
%{_libdir}/kde3/kfile_kplayer.la
%attr(755,root,root) %{_libdir}/kde3/kfile_kplayer.so
%{_libdir}/kde3/libkplayerpart.la
%attr(755,root,root) %{_libdir}/kde3/libkplayerpart.so
%{_datadir}/apps/kplayer
%{_desktopdir}/kplayer.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/locolor/*/apps/*.png
%{_datadir}/services/kplayerpart.desktop
%{_datadir}/services/kfile_kplayer.desktop
%{_datadir}/services/mmst.protocol
%{_datadir}/services/mmsu.protocol
%{_datadir}/services/pnm.protocol
