#include <stdio.h>


class parent {
public:
	int i = 7;
	virtual int get() {
		return i;
	}
};

class child : public parent {
public:
	int i = 5;
	int get() {
		return i;
	}
};

int main() {
	parent *p = new child();
	child *c = new child();
	printf("p->i : %d\n", p->i);
	printf("p->get() : %d\n", p->get());
	printf("c->i : %d\n", c->i);
	printf("c->get() : %d\n", c->get());

	delete(p);
	delete(c);

	return 0;
}