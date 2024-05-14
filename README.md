PYTEST

Pytest, Python kullanırken daha okunaklı, daha pratik ve daha düzenli kodlar yazmamıza olanak sağlayan bir framework'tür. Pytest basit bir sintaksa sahip olması ve açık kaynak kodlu olmasıyla ön plana çıkmaktadır.
Pytest birtakım özel işlevlere sahip built-in fonksiyonları kullanıma sunar. Bunlar Pytest bağlamında "dekoratör" olarak adlandırılır ve önlerine "@" işareti alırlar.

Mevzubahis dekoratörlerden bazıları aşağıdaki gibidir:

@pytest.fixture: Bir test kodunu diğer test kodları için bir baz haline getirmek için kullanılır. Fixture ile bir test için önkoşul ve veri seti oluşturabilir veya test bittikten sonra teardown işlevi atayabilirsiniz.

@pytest.mark: Bir testi işaretlemek veya birkaç test bloğunu gruplandırmak amacıyla kullanılır. Pytest'in sağladığı built-in marker'lar haricinde kendi isimlendirmelerinizle özgün marker'lar oluşturabilirsiniz.

@pytest.mark.parametrize: Bir test için birden fazla parametre kullanılması gerektiğinde bu dekoratör kullanılabilir. Aynı testi farklı girdilerle çalıştırma imkanı sunar.

@pytest.mark.skip: Belirli testlerin koşulmasını atlamak için kullanılır.

@pytest.mark.xfail: Bu dekoratör, bir testin beklenen bir hata üretmesini ve bu hatanın başarısızlık olarak değil, bir beklenti olarak kabul edilmesini sağlar.

@pytest.mark.timeout: Bir testin belirli bir süre içinde tamamlanması gerektiğini belirtmek için kullanılır. Test belirlenen süre içinde tamamlanmazsa testi başarısız olarak kabul eder.

@pytest.mark.dependency: Bir testin başka bir teste bağımlı olarak koşulmasını sağlar.
