import java.util.*;
/*
@author: Jacobo David Estefania
*/
public class HeldKarpAlgorythm {

    private static int INFINITY = Integer.MAX_VALUE;

    private static class Index {
        int vActual;
        Set<Integer> Vertices;

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Index index = (Index) o;

            if (vActual != index.vActual) return false;
            return !(Vertices != null ? !Vertices.equals(index.Vertices) : index.Vertices != null);
        }

        @Override
        public int hashCode() {
            int sol = vActual;
            sol = 31 * sol + (Vertices != null ? Vertices.hashCode() : 0);
            return sol;
        }

        private static Index createIndex(int vertex, Set<Integer> Vertices) {
            Index i = new Index();
            i.vActual = vertex;
            i.Vertices = Vertices;
            return i;
        }
    }

    private static class SetSizeComparator implements Comparator<Set<Integer>>{
        @Override
        public int compare(Set<Integer> o1, Set<Integer> o2) {
            return o1.size() - o2.size();
        }
    }

    public int minimo(int[][] distance) {

        Map<Index, Integer> minimoDP = new HashMap<>();
        Map<Index, Integer> parent = new HashMap<>();

        List<Set<Integer>> allSets = generateCombination(distance.length - 1);

        for(Set<Integer> set : allSets) {
            for(int vActual = 1; vActual < distance.length; vActual++) {
                if(set.contains(vActual)) {
                    continue;
                }
                Index index = Index.createIndex(vActual, set);
                int minimo = INFINITY;
                int minverticeA = 0;
                Set<Integer> copySet = new HashSet<>(set);
                for(int verticeA : set) {
                    int cost = distance[verticeA][vActual] + getCost(copySet, verticeA, minimoDP);
                    if(cost < minimo) {
                        minimo = cost;
                        minverticeA = verticeA;
                    }
                }
                if(set.size() == 0) {
                    minimo = distance[0][vActual];
                }
                minimoDP.put(index, minimo);
                parent.put(index, minverticeA);
            }
        }
        Set<Integer> set = new HashSet<>();
        for(int i=1; i < distance.length; i++) {
            set.add(i);
        }
        int min = Integer.MAX_VALUE;
        int verticeA = -1;
        Set<Integer> copySet = new HashSet<>(set);
        for(int k : set) {
            int cost = distance[k][0] + getCost(copySet, k, minimoDP);
            if(cost < min) {
                min = cost;
                verticeA = k;
            }
        }
        parent.put(Index.createIndex(0, set), verticeA);
        printTour(parent, distance.length);
        return min;
    }

    private int getCost(Set<Integer> set, int verticeA, Map<Index, Integer> minimoDP) {
        set.remove(verticeA);
        Index index = Index.createIndex(verticeA, set);
        int cost = minimoDP.get(index);
        set.add(verticeA);
        return cost;
    }

    private void printTour(Map<Index, Integer> parent, int totalVertices) {
        Set<Integer> set = new HashSet<>();
        for(int i=0; i < totalVertices; i++) {
            set.add(i);
        }
        Integer start = 0;
        Deque<Integer> stack = new LinkedList<>();
        while(true) {
            stack.push(start);
            set.remove(start);
            start = parent.get(Index.createIndex(start, set));
            if(start == null) {
                break;
            }
        }
        StringJoiner joiner = new StringJoiner("->");
        stack.forEach(v -> joiner.add(String.valueOf(v)));
        System.out.println("\nTSP tour");
        System.out.println(joiner.toString());
    }

    private List<Set<Integer>> generateCombination(int n) {
        int input[] = new int[n];
        for(int i = 0; i < input.length; i++) {
            input[i] = i+1;
        }
        List<Set<Integer>> allSets = new ArrayList<>();
        int sol[] = new int[input.length];
        generateCombination(input, 0, 0, allSets, sol);
        Collections.sort(allSets, new SetSizeComparator());
        return allSets;
    }

 private static Set<Integer> llenarSet(int input[], int pos) {
        if(pos == 0) {
            return new HashSet<>();
        }
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i < pos; i++) {
            set.add(input[i]);
        }
        return set;
    }

    private void generateCombination(int input[], int start, int pos, List<Set<Integer>> allSets, int sol[]) {
        if(pos == input.length) {
            return;
        }
        Set<Integer> set = llenarSet(sol, pos);
        allSets.add(set);
        for(int i=start; i < input.length; i++) {
            sol[pos] = input[i];
            generateCombination(input, i+1, pos+1, allSets, sol);
        }
    }

   
}