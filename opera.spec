%define     code 1583
%define     namecode 32633

Name:       opera-next
Version:    12.50
Release:    %{code}.1%{?dist}
Summary:    Web Browser for Linux
Summary(ru):Веб-браузер для Linux
Epoch:      5

Group:      Applications/Internet
License:    Proprietary
URL:        http://www.opera.com
Source1:    http://snapshot.opera.com/unix/%{namecode}_%{version}-%{code}/%{name}-%{version}-%{code}.i386.rpm
Source0:    http://snapshot.opera.com/unix/%{namecode}_%{version}-%{code}/%{name}-%{version}-%{code}.x86_64.rpm

BuildRequires:  desktop-file-utils


%description
Welcome to the Opera Web browser.  It is smaller, faster,
customize, powerful, yet user-friendly.  Opera
eliminates sluggish performance, HTML standard violations,
desktop domination, and instability.  This robust Web
browser lets you navigate the Web at incredible speed and
offers you the best Internet experience.

%description -l ru
Добро пожаловать в веб-браузер Opera. Opera отличается малыми
размерами, скоростью загрузки HTML документов как из Интернета,
так и с локального диска, универсальностью в загрузке и
отображении веб-страниц, богатством настроек и абсолютной
функциональностью. Благодаря многообразию своих настроек,
Opera может помочь вам сберечь драгоценное онлайновое время
и работать с вашим компьютером наиболее эффективно, то есть
использовать Opera как профессиональный броузер, управляя выводом
графических изображений, использованием каскадных таблиц стилей и
интерфейсом.

%ifarch x86_64
%package    pluginwrapper
Summary:    32bit wrapper for 64bit browser
Summary(ru):32бит обёртка для 64бит версии браузера
Group:      Applications/Internet
Requires:   %{name} = %{epoch}:%{version}-%{release}


%description pluginwrapper
This package contains 32bit wrapper for 64bit browser

%description pluginwrapper -l ru
Этот пакет содержит 32бит обёртку для 64бит версии браузера
%endif


%prep
%setup -q -c -T


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
pushd %{buildroot}
%ifarch x86_64
rpm2cpio %{SOURCE0} | cpio -idV --quiet
%else
rpm2cpio %{SOURCE1} | cpio -idV --quiet
%endif
popd

mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_datadir}/doc/%{name}-%{version}

desktop-file-install --vendor rfremix \
  --dir %{buildroot}%{_datadir}/applications \
  --add-category Network \
  --add-category WebBrowser \
  --add-category X-Fedora \
  --delete-original \
  %{buildroot}%{_datadir}/applications/%{name}-browser.desktop

# we do not need these files as default license is present
rm -f %{buildroot}%{_datadir}/%{name}/locale/*/license.txt

# install license
rm -f %{buildroot}%{_datadir}/%{name}/defaults/license.txt
cp %{buildroot}%{_datadir}/doc/%{name}-%{version}/LICENSE \
	%{buildroot}%{_datadir}/%{name}/defaults/license.txt

# unkhardlink
# rm %{buildroot}%{_datadir}/%{name}/locale/zh-tw/browser.js
# cp %{buildroot}%{_datadir}/%{name}/locale/zh-cn/browser.js \
#     %{buildroot}%{_datadir}/%{name}/locale/zh-tw/browser.js


%post
update-desktop-database &> /dev/null || :
touch --no-create /usr/share/icons/hicolor &>/dev/null || :
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet /usr/share/icons/hicolor || :
fi


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create /usr/share/icons/hicolor &>/dev/null
    gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :


%posttrans
gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :


%files
%doc %{_datadir}/doc/%{name}-%{version}
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_datadir}/icons/*
%{_datadir}/mime/*
%{_datadir}/applications/*.desktop

%ifarch x86_64
%exclude %{_libdir}/%{name}/pluginwrapper/operapluginwrapper-ia32-linux

%files pluginwrapper
%{_libdir}/%{name}/pluginwrapper/operapluginwrapper-ia32-linux
%endif


%changelog
* Sat Sep 08 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.50.1583-1.R
- Update to 12.50.1583

* Thu Jun 14 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1467-1.R
- Update to 12.00.1467

* Thu May 10 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1387-1.R
- Update to 12.00.1387

* Wed Apr 18 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1372-1.R
- Update to 12.00.1372

* Sat Feb 25 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1312-1.R
- Update to 12.00.1312

* Thu Dec 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1213-1.R
- Update to 12.00.1213

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1155-1.R
- Added description in russian language
- Update to 12.00.1155

* Mon Nov 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1116-1.R
- update to 12.00.1116

* Tue Oct 11 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1090-1.R
- update to 12.00.1090

* Wed Sep 28 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1076-1.R
- update to 12.00.1076

* Wed Sep 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1065-1.R
- update to 12.00.1065
- corrected requires for 

* Fri Sep 09 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1060-1.R
- update to 12.00.1060

* Tue Sep 02 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1054-1.R
- update to 12.00.1054

* Tue Aug 16 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1047-1.R
- update to 12.00.1047

* Sat Aug 06 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1042-1.R
- update to 12.00.1042

* Thu Aug 04 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 5:12.00.1039-1.R
- update to 12.00.1039

* Tue Jun 27 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 5:11.50-1.R
- update to 11.50

* Tue Apr 12 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 5:11.10-2
- fix license window

* Tue Apr 12 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 5:11.10-1
- update to 11.10

* Thu Jan 27 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 5:11.01-1
- update to 11.01

* Thu Dec 16 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 5:11.00-1
- update to 11.00

* Tue Oct 12 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 5:10.63-2
- put 32bit binary to separate package

* Tue Oct 12 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.63-1
- update to 10.63

* Mon Sep 20 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.62-1
- update to 10.62

* Fri Aug 13 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.61-1
- update to 10.61

* Thu Jul  1 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.60-1
- update to 10.60

* Wed Jun 30 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.11-1
- update to 10.11

* Tue Jun  1 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.10-1
- update to 10.10

* Wed Oct 28 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.01-1
- update to 10.01

* Tue Sep 15 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.00-2
- qt4 version

* Mon Sep  7 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.00-1
- update to final 10.00

* Fri Jul 17 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.00-0.3.beta2
- update to beta2

* Wed Jun 24 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.00-0.2.beta1
- we had problem for F11 i586 arch in spec file. Fixed now.

* Wed Jun  3 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.00-0.1.beta1
- update to 10.00 beta 1

* Wed Mar  4 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 9.64-1
- update to 9.64

* Tue Dec 16 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.63-1
- update to 9.63

* Wed Oct 30 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.62-1
- update to 9.62

* Tue Oct 21 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.61-1
- update to 9.61

* Wed Oct  8 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.60-1
- update to 9.60

* Mon Aug 25 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.52-1
- update to 9.52

* Fri Jul  4 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.51-1
- update to 9.51

* Fri Jun 13 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.50-1
- final 9.50

* Thu Jun 12 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.50-0.2034
- update to RC

* Wed May 21 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.50b2-0.1
- add opera.desktop file

* Mon Apr 28 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.50b2-0
- update to 9.50b2

* Thu Apr  3 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.27-1
- 9.27

* Wed Feb 20 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.26-1
- 9.26

* Thu Dec 20 2007 Arkady L. Shane <ashejn@yandex-team.ru> - 9.25-1
- 9.25

* Thu Aug 16 2007 Arkady L. Shane <ashejn@yandex-team.ru> - 9.23-1
- 9.23

* Thu Jul 19 2007 Arkady L. Shane <ashejn@yandex-team.ru> - 9.22-1
- 9.22

* Wed Jun 20 2007 Arkady L. Shane <ashejn@yandex-team.ru> - 9.21-2
- add R for qt 3

* Thu May 17 2007 Arkady L. Shane <ashejn@yandex-team.ru> - 9.21-1
- 9.21

* Thu Apr 12 2007 Arkady L. Shane <ashejn@yandex-team.ru> - 9.20-0%{?dist}
- 9.20

* Fri Dec 22 2006 Arkady L. Shane <ashejn@yandex-team.ru> - 9.10-0%{?dist}
- 9.10

* Wed Jun 21 2006 Arkady L. Shane <shejn@msiu.ru> - 9.0-1%{?dist}
- rebuilt package with russian langpack
