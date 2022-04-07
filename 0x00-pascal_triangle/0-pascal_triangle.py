def pascal(p):

        P = [[1],[1, 1]]

            if p < 3: return P[0:p]

                while len(P) < p:

                            last = P[-1]

                                    layer = [1]

                                            for i in xrange(len(last)-1):

                                                            layer.append(last[i]+last[i+1])

                                                                    layer.append(1)

                                                                            P.append(layer)

                                                                                return P
