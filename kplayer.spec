Summary:	KDE media player based on mplayer
Summary(pl):	Odtwarzacz mediów dla KDE bazuj±cy na mplayerze
Name:		kplayer
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-src.tar.bz2
# Source0-md5:	9a7eebb9aac656e070cf82eb959ff9bb
URL:		http://sourceforge.net/projects/kplayer/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1
Requires:	kdelibs >= 3.1
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KPlayer is a KDE media player based on mplayer.

%description -l pl
KPlayer to odtwarzacz mediów dla KDE bazuj±cy na mplayerze.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kplayer
%{_datadir}/apps/kplayer
%{_applnkdir}/Multimedia/kplayer.desktop
%{_pixmapsdir}/*/*/apps/*.png
%{_libdir}/kde3/kfile_kplayer.la
%{_libdir}/kde3/kfile_kplayer.so
%{_libdir}/kde3/libkplayerpart.la
%{_libdir}/kde3/libkplayerpart.so
%{_datadir}//services/kplayerpart.desktop
#%{_datadir}/services/*
